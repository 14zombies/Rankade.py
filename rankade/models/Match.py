# Match.py

import json
from dataclasses import InitVar, dataclass, field
from typing import Any, Dict, List, Optional, Type
from datetime import date

from rankade.api.Endpoint import Endpoint
from .Base import RankadeObject, ResultList
from .Error import Error
from .Faction import Faction
from .Game import Game
from .Base import Page
from .Player import Player


@dataclass
class Match(RankadeObject):

    weight: str
    weightLabel: str
    notes: str
    id: Optional[str] = field(default=None)
    externalId: Optional[str] = field(default=None)
    date: Optional[str] = field(default=None)
    registrationDate: Optional[str] = field(default=None)
    number: Optional[int] = field(default=None)
    summary: Optional[str] = field(default=None)
    type: Optional[str] = field(default=None)
    draw: Optional[int] = field(default=None)
    game: InitVar[dict]  # type: ignore
    _game: Optional[Game] = field(default=None, init=False)
    factions: InitVar[List]  # type: ignore
    _factions: List = field(default_factory=list, init=False)

    def __post_init__(self, game, factions):
        self._game = Game(**game)
        for faction in factions:
            self._factions.append(
                Faction(**faction))

    @property
    def is_draw(self):
        return bool(self.draw)

    @property
    def winning_factions(self):
        return [faction for faction in self.factions if faction.rank == 1]

    @property
    def winning_players(self):
        faction_players = [
            faction.players for faction in self.winning_factions]
        return [player for faction in faction_players for player in faction]

    @property
    def factions(self) -> List[Faction]:
        return self._factions

    @property
    def game(self) -> Optional[Game]:
        return self._game

    def add_faction(self, players, rank, points):
        # if not isinstance(players, [rankade.Player.Player]):
        #     raise Exception
        if not isinstance(rank, int):
            raise Exception
        if not isinstance(points, str):
            raise Exception
        if len(players) < 1:
            raise Exception
        players_dict = []
        for player in players:
            if player.id == "bot" and len(players) > 1:
                # A bot faction cannot contain any players.
                Exception

            players_dict.append(player.__dict__)

        faction = Faction(self._api, points=points, rank=rank, players=players_dict)
        self._factions.append(faction)

    def add_bot_faction(self, rank, points):
        bot_player = Player(self._api, id="bot", ghost=0, displayName="bot", icon="")
        self.add_faction(bot_player, rank, points)

    async def save(self):
        if self.id is not None:
            raise Exception()
        new_match_endpoint = Endpoint.MATCH
        new_match_endpoint.set_json(self.to_json())
        await self._api.request(new_match_endpoint)

    def to_json(self):
        json_factions = [f.to_json() for f in self._factions]
        match = [{
            "game": self._game.id,
            "weight": self._game.weight,
            "factions": json_factions,
            "notes": self.notes
        }]
        return match


@dataclass
class Matches(Page):

    """Represents the a Matches page, returned by Rankade API.

    Attributes
    ----------
    matches : [Match]
        Individual Match objects returned by the server.
    page : int
        Page number.
    rowsForPage : int
        Max number of Match objects per page.
    totalMatches : int
        Total matches on all pages.
    totalPages : int
        Total number of pages.

    Methods
    -------
    next_page
        Returns the next page or None if last page.
    """

    totalMatches: InitVar[int]
    _content_class: Type = field(init=False, default=Match)


@dataclass
class MatchStatus(RankadeObject):
    """Retrieves API-recorded matches status.
    Details: https://rankade.com/api/#get-matches-status

    Attributes
    ----------
    added : int
        Matches added to subset(s), both processed and not yet processed.
    processed : int
        Processed matches.
    queued : int
        Accepted matches, queued for insertion.
    total : int
        Total API-recorded matches.
    waiting : int
        Inserted matches, waiting for their subset(s).

    Notes
    -----
    Counts are only for matches entered via API.
    Matches entered via webapp/app are not included.
    """

    added: int
    processed: int
    queued: int
    total: int
    waiting: int


@dataclass
class NewMatchReturn(RankadeObject):

    index: int
    id: Optional[str]
    name: Optional[str]
    errors: InitVar[Dict]  # type: ignore
    _errors: List[Error] = field(default_factory=list, init=False)

    def __post_init__(self, errors):
        for item in errors:
            self._errors.append(Error(self._api, **item))

    @property
    def errors(self):
        return self._errors


@dataclass
class NewMatchResponse(ResultList):

    total: int
    acceptedCount: int
    rejectedCount: int
    rejected: InitVar[dict]  # type: ignore
    accepted: InitVar[dict]  # type: ignore
    data: Any = field(default=None, init=False)
    _rejected: List[NewMatchReturn] = field(default_factory=list, init=False)
    _content_class: Type = field(default=NewMatchReturn, init=False)

    def __post_init__(self, rejected, accepted):
        for item in rejected:
            self.rejected.append(NewMatchReturn(self._api, **item))
        return super().__post_init__(accepted)

    @property
    def rejected(self):
        return self._rejected

    @property
    def accepted(self):
        return self.data

    @property
    def has_error(self) -> bool:
        return len(self.rejected) > 0
