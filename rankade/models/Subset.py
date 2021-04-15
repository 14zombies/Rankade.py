# Subset.py

from dataclasses import InitVar, dataclass, field
from typing import Dict, List, Optional, Type

from .Base import RankadeObject, ResultList
from .Game import Game
from .Match import Match


@dataclass
class Subset(RankadeObject):
    id: str
    name: str
    type: str
    creationDate: str
    isMain: int
    isCustom: int
    icon: str
    countMatches: int
    _game: Optional[Game] = field(default=None, init=False)
    _firstMatch: Optional[Match] = field(default=None, init=False)
    _lastMatch: Optional[Match] = field(default=None, init=False)
    game: InitVar[Optional[Dict]] = field(default=None)  # type: ignore
    firstMatch: InitVar[Optional[Dict]] = field(default=None)  # type: ignore
    lastMatch: InitVar[Optional[Dict]] = field(default=None)  # type: ignore

    def __post_init__(self, game, firstMatch, lastMatch):
        if isinstance(game, dict):
            self._game = Game(self._api, **game)
        if isinstance(firstMatch, dict):
            self._firstMatch = Match(self._api, **firstMatch)
        if isinstance(lastMatch, dict):
            self._lastMatch = Match(self._api, **lastMatch)

    @property
    def game(self) -> Optional[Game]:
        return self._game

    @property
    def firstMatch(self) -> Optional[Match]:
        return self._firstMatch

    @property
    def lastMatch(self) -> Optional[Match]:
        return self._lastMatch

    def all_matches(self):
        pass


@dataclass
class Subsets(ResultList):

    _content_class: Type = field(init=False, default=Subset)

