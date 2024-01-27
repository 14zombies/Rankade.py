# rankade.models.Game.py
from dataclasses import dataclass, field
from typing import ClassVar, Optional, Type

from .Base import RankadeObject, ResultList


@dataclass(kw_only=True, slots=True)
class Game(RankadeObject):
    """Represents a single Game object returned by Rankade"""

    id: int
    """Rankade id of the game."""
    name: str
    """ Game name."""
    weight: str
    """ Should be one of ultralight, light, midlight, normal, heavy, massive.
    A heavier game will result in a larger variation of the ree score."""
    weightLabel: str
    """Appears to be a nicely formatted version of the weight attribute."""
    mediumImage: str
    """URL for game art."""
    thumbnail: str
    """URL for game art thumbnail."""
    bggIdGame: Optional[int] = field(default=None)
    """Board Game Geek id for the game."""


@dataclass(kw_only=True, slots=True)
class Games(ResultList[Game]):
    """
    Represents the list of Games returned by the Rankade server.
    Individual game objects returned by the server can be accessed in the same way as a regular list.
    """

    _content_class: ClassVar[Type[RankadeObject]] = Game
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""
