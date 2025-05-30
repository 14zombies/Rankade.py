"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import ClassVar, Optional, Type

from .Base import RankadeObject, ResultList

"""
This type stub file was generated by pyright.
"""
@dataclass(kw_only=True, slots=True)
class Game(RankadeObject):
    """Represents a single Game object returned by Rankade"""
    id: int
    name: str
    weight: str
    weightLabel: str
    mediumImage: str
    thumbnail: str
    bggIdGame: Optional[int] = ...


@dataclass(kw_only=True, slots=True)
class Games(ResultList[Game]):
    """
    Represents the list of Games returned by the Rankade server.
    Individual game objects returned by the server can be accessed in the same way as a regular list.
    """
    _content_class: ClassVar[Type[RankadeObject]] = ...


