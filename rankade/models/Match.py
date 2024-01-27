# rankade.models.Match.py
from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, Dict, List, Type

from .Base import Page, RankadeObject
from .Faction import Faction, Factions
from .Game import Game
from .Player import Player, Players


@dataclass(kw_only=True, slots=True)
class Match(RankadeObject):
    weight: str
    weightLabel: str
    notes: str
    id: str
    externalId: str
    date: datetime
    registrationDate: datetime
    number: int
    summary: str
    type: str
    draw: bool
    game: Game
    factions: Factions

    def __post_init__(self):
        if isinstance(self.draw, (str, int)):  # pyright: ignore[reportUnnecessaryIsInstance]
            self.draw = bool(self.draw)
        if isinstance(self.date, str):
            self.date = datetime.fromisoformat(self.date)
        if isinstance(self.registrationDate, str):
            self.registrationDate = datetime.fromisoformat(self.registrationDate)
        if isinstance(self.game, Dict):
            self.game = Game(**self.game)  # pyright: ignore[reportUnknownArgumentType]

        if isinstance(self.factions, (List, Dict)):
            if not isinstance(self.factions[0], Faction):  # pyright: ignore[reportUnnecessaryIsInstance]
                self.factions = Factions.from_dict(data_dict=self.factions)  # pyright: ignore[reportArgumentType]
            self.factions.sort(key=lambda f: f.rank)

    @property
    def is_draw(self) -> bool:
        return bool(self.draw)

    @property
    def winning_factions(self) -> List[Faction]:
        return [faction for faction in self.factions if faction.rank == 1]

    @property
    def winning_players(self) -> List[Player]:
        faction_players = [faction.players for faction in self.winning_factions]
        return [player for faction in faction_players for player in faction]

    @property
    def players(self) -> Players:
        players = [faction.players for faction in self.factions]
        flat_players = [x for xs in players for x in xs]
        return Players(data=flat_players)

    @property
    def player_ids(self) -> List[str]:
        return [p.id for p in self.players]


@dataclass(kw_only=True, slots=True)
class Matches(Page[Match]):

    """
    Represents a list of match objects returned by the Rankade server.
    Individual match objects returned by the server can be accessed in the same way as a regular list.
    """

    totalMatches: int
    """Total matches on all pages."""
    _content_class: ClassVar[Type[RankadeObject]] = Match
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""

    def all_players(self) -> Players:
        """Returns all players from all factions of all matches."""
        players = [player for match_players in self.data for player in match_players.players]
        deduped_players = [player for count, player in enumerate(players) if player not in players[count + 1 :]]
        return Players(data=deduped_players)
