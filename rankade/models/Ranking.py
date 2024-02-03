# rankade.models.Ranking.py
from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Dict, Self, Type

from .Base import Page, RankadeObject, ResultList
from .Match import Match
from .Player import Player
from .Subset import Subset


@dataclass(kw_only=True)
class Ranking(RankadeObject):
    """Individual Ranking of a player in the subset."""

    ree: int
    """Player's Ree score. (In the subset or after selected match.)"""
    deltaRee: int
    """Player's change in Ree score. (In the subset or after selected match.)"""
    position: int
    """Player's position. (In the subset or after selected match.)"""
    deltaPosition: int
    """Players change in position. (In the subset or after selected match.)"""
    belt: int
    """
    Players belt. [What are belts](https://rankade.com/frequently-asked-question/2/what-are-belts/54)
    """
    beltLabel: str
    """
    Label of players belt:
    - White belt: 9th Kyū - Kyūkyū - 九級
    - Yellow belt: 8th Kyū - Hakkyū - 八級
    - Orange belt: 7th Kyū - Nanakyū - 七級
    - Green belt: 6th Kyū - Rokkyū - 六級
    - Blue belt 1st level: 5th Kyū - Gokyū - 五級
    - Blue belt 2nd level: 4th Kyū - Yonkyū - 四級
    - Brown belt 1st level: 3rd Kyū - Sankyū - 三級
    - Brown belt 2nd level: 2nd Kyū - Nikyū - 二級
    - Brown belt 3rd level: 1st Kyū - Ikkyū - 一級
    - Black belt
    """
    title: int
    """
    Players Rank title:
    1. Samurai
    2. Daimyo
    3. Shogun
    4. Emperor
    """
    titleLabel: str
    """Players Rank title."""
    status: int
    """
    Players status:
    1.  Inactive player
    2.  Semi-active player
    3.  Nearly active player
    4.  Active player
    """
    statusLabel: str
    """Players status."""
    player: Player
    """Player object"""

    def __post_init__(self) -> None:
        if isinstance(self.player, Dict):
            self.player = Player(**self.player)  # pyright: ignore[reportUnknownArgumentType]


@dataclass(kw_only=True, slots=True)
class Rankings(ResultList[Ranking], Page):
    """
    Represents the list of Rankings returned by the Rankade server.
    Individual ranking objects returned by the server can be accessed in the same way as a regular list.
    """

    _content_class: ClassVar[Type[RankadeObject]] = Ranking
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""

    match: Match
    """Match after which the rankings were calculated"""
    subset: Subset
    """Subset which the ranking applies to."""

    def __post_init__(self) -> None:
        if isinstance(self.match, Dict):
            self.match = Match(**self.match)  # pyright: ignore[reportUnknownArgumentType]

        if isinstance(self.subset, Dict):
            self.subset = Subset(**self.subset)  # pyright: ignore[reportUnknownArgumentType]

        self.data.sort(key=lambda position: position.position)

    @property
    def sorted_by_position(self) -> Self:
        """Rankings sorted by position."""
        r = self[:]
        r.sort(key=lambda position: position.position)
        return r

    @property
    def sorted_by_delta_position(self) -> Self:
        """Rankings sorted by change of position."""
        r = self[:]
        r.sort(reverse=True, key=lambda position: position.deltaPosition)
        return r

    @property
    def sorted_by_ree(self) -> Self:
        """Rankings sorted by Ree score."""
        r = self[:]
        r.sort(reverse=True, key=lambda position: position.ree)
        return r

    @property
    def sorted_by_delta_ree(self) -> Self:
        """Rankings sorted by change of Ree score."""
        r = self[:]
        r.sort(reverse=True, key=lambda position: position.deltaRee)
        return r
