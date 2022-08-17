# Ranking.py

from dataclasses import InitVar, dataclass, field
from typing import Optional, Type

from .Base import RankadeObject
from .Match import Match
from .Base import Page
from .Player import Player
from .Subset import Subset


@dataclass(order=True)
class Ranking(RankadeObject):

    ree: int
    deltaRee: int
    position: int
    deltaPosition: int
    belt: int
    beltLabel: str
    title: int
    titleLabel: str
    status: int
    statusLabel: int
    player: InitVar[dict]  # type: ignore
    _player: Optional[Player] = field(
        default=None, init=False)

    def __post_init__(self, player):
        self._player = Player(self._api, **player)

    @property
    def player(self):
        return self._player


@dataclass
class Rankings(Page):

    _content_class: Type = field(init=False, default=Ranking)
    match: InitVar[dict]  # type: ignore
    subset: InitVar[dict]  # type: ignore
    _match: Optional[Match] = field(default=None, init=False)
    _subset: Optional[Subset] = field(default=None, init=False)

    def __post_init__(self, data, match, subset, *args):
        if isinstance(match, dict):
            self._match = Match(self._api, **match)
        elif isinstance(match, Match):
            self._match = match

        if isinstance(subset, dict):
            self._subset = Subset(self._api, **subset)
        elif isinstance(subset, Subset):
            self._subset = subset
        return super().__post_init__(data)

    @property
    def match(self):
        return self._match

    @property
    def subset(self):
        return self._subset

    @property
    def sorted_by_delta_position(self):
        r = self.data[:]
        r.sort(reverse=True, key=lambda position: position.deltaPosition)
        return r

    @property
    def sorted_by_delta_ree(self):
        r = self.data[:]
        r.sort(reverse=True, key=lambda position: position.deltaRee)
        return r
