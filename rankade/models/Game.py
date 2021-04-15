# Game.py

from dataclasses import dataclass, field
from typing import Any, List, Optional, Type

from .Base import RankadeObject, ResultList



@dataclass
class Game(RankadeObject):

    """Represents a single Game object returned by Rankade

    Attributes
    ----------
    id : str
        Rankade id of the game.
    name : str
        Games name.
    weight : str
        Should be ultralight, light, midlight, normal, heavy, massive.
        A heavier game will result in a larger variation of the ree score.
    weightLabel : str
        Appears to be a nicely formatted version of the weight attribute.
    mediumImage : str
        URL for game art.
    thumbnail : str
        URL for game art thumbnail.
    bggIdGame : Optional[int]
        Board Game Geek id for the game.
    """

    id: str
    name: str
    weight: str
    weightLabel: str
    mediumImage: str
    thumbnail: str
    bggIdGame: Optional[int] = None

    async def get_matches(self):
        pass

@dataclass
class Games(ResultList):
    """Represents the list of Games returned by the Rankade
    server.

    Attributes
    ----------
    games : [Game]
        Individual game objects returned by the server.
    """

    _content_class: Type = field(init=False, default=Game)
