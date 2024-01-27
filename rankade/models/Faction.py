# rankade.models.Faction.py
from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Type

from rankade.api.Api import JSON

from ..Consts import BOT_ID
from .Base import RankadeObject, ResultList
from .Player import Players


@dataclass(kw_only=True, slots=True)
class Faction(RankadeObject):
    """Represents a faction used within a Match."""

    name: str
    """Faction Name"""
    points: str
    """Faction points/score,"""
    rank: int
    """Faction ranking compared to other factions."""
    bot: bool = False
    """returns true if faction is bot faction."""
    winner: bool = False
    """returns true if faction is winning faction."""
    players: Players
    """List of faction players."""
    countPlayers: int = 0
    """Number of players in the faction."""

    def __post_init__(self):
        if isinstance(self.bot, int) or self.players[0].id == BOT_ID:  # pyright: ignore[reportUnnecessaryIsInstance]
            self.bot = bool(self.bot)
        if isinstance(self.winner, int):  # pyright: ignore[reportUnnecessaryIsInstance]
            self.winner = bool(self.winner)
        if not isinstance(self.players, Players):  # pyright: ignore[reportUnnecessaryIsInstance]
            self.players = Players.from_dict(data_dict=self.players)
        self.countPlayers = len(self.players)

    @property
    def is_bot(self) -> bool:
        """Convenience attribute - returns true if faction is bot faction."""
        return self.bot

    @property
    def is_winner(self) -> bool:
        """Convenience attribute - returns true if faction is winning faction."""
        return self.winner

    def as_dict(self) -> JSON:
        """
        Returns a custom dictionary for new match server post request.
        """
        ids: JSON = [str(p.id) for p in self.players]
        faction_dict: JSON = {
            "rank": int(self.rank),
            "score": str(self.points),
            "players": ids,
        }
        return faction_dict


@dataclass(kw_only=True, slots=True)
class Factions(ResultList[Faction]):
    """
    Represents a list of faction objects returned by the Rankade server.
    Individual faction objects returned by the server can be accessed in the same way as a regular list.
    """

    _content_class: ClassVar[Type[RankadeObject]] = Faction
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""
