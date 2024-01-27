# rankade.models.NewMatch.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional, Type, Union

from rankade.api.Api import JSON
from rankade.RankadeExceptions import RankadeException

from ..Consts import BOT_ID
from .Base import RankadeObject, ResultList
from .Faction import Faction, Factions
from .Game import Game
from .Player import Player, Players


@dataclass
class NewMatch(RankadeObject):
    """This class to be used for creating Matches to post to the Rankade API."""

    notes: str
    """General notes."""
    name: str = ""
    """
    Match name.
    :::{note}
    Use any custom string for the name of the match or 2 special options are available:

    "default_1"
        : set game's name as the match name.

    "default_2"
        : to set faction/player name vs other faction/player name as the match name.
    :::
    """
    game: Optional[Game] = field(default=None)
    """Game id retrieved from ` GET /games/search`, `GET /games`, or `GET /games/popular` API calls."""
    factions: Optional[Factions] = field(default=None)
    """Factions' data."""
    weight: str = field(default="normal")
    """Match weight, chosen from this list: ultralight, light, midlight, normal, heavy, massive.
    A heavier game results in larger variations in ree score, a lighter game in smaller ones. We strongly suggest you to set weights in a way that most of the matches have normal weight. See FAQ for details."""

    def add_bot_faction(self, rank: int, points: str, name: str = ""):
        """
        Convenience method to add a bot faction to the match.
        """
        bot_player = Players(data=[Player(id=BOT_ID, ghost=False, displayName=BOT_ID, icon="")])
        self.add_faction(players=bot_player, rank=rank, points=points, name=name, bot=True)

    def add_faction(self, players: Union[Players, Player], rank: int, points: str, name: str = "", bot: bool = False):
        """
        Convenience method to add a faction to the match.
        """
        if isinstance(players, Player):
            players = Players(data=[players])
        if len(players) < 1:
            raise RankadeException(message="A faction must contain at least 1 player")
        bot_players = [player for player in players if player.id == BOT_ID]
        if len(bot_players) > 1 or (bot and len(players) > 1):
            raise RankadeException(message="A bot faction cannot contain any other players")

        faction = Faction(points=points, rank=rank, players=players, name=name, bot=bot)
        if self.factions is None:
            self.factions = Factions(data=[faction])
        else:
            self.factions.append(faction)

    def as_dict(self) -> JSON:
        """
        Returns a custom dictionary for new match server post request.
        """
        if self.game is None or self.factions is None:
            return []
        factions = [f.as_dict() for f in self.factions]
        match: JSON = {
            "name": self.name,
            "game": self.game.id,
            "weight": self.weight or self.game.weight,
            "factions": factions,
            "notes": self.notes,
        }
        return [match]


@dataclass
class NewMatchList(ResultList[NewMatch]):
    """
    Represents the list of NewMatches returned by the Rankade server.
    Individual NewMatch objects returned by the server can be accessed in the same way as a regular list.
    """

    _content_class: ClassVar[Type[RankadeObject]] = NewMatch
    """ClassVar to allow the an object in the list to be created from a dict returned from the server."""
