# rankade.models.Ranking.py
from dataclasses import dataclass
from typing import ClassVar, Dict, Type

from .Base import Page, RankadeObject
from .Match import Match
from .Player import Player
from .Subset import Subset


@dataclass(kw_only=True, slots=True)
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
    """Players current belt."""
    beltLabel: str
    """Label of players current belt."""
    title: int
    """Players Rank title."""
    titleLabel: str
    """Players Rank title."""
    status: int
    """Players status."""
    statusLabel: str
    """Players status."""
    player: Player
    """Player object"""

    def __post_init__(self):
        if isinstance(self.player, Dict):
            self.player = Player(**self.player)  # pyright: ignore[reportUnknownArgumentType]


@dataclass(kw_only=True, slots=True)
class Rankings(Page[Ranking]):
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

    def __post_init__(self):
        if isinstance(self.match, Dict):
            self.match = Match(**self.match)  # pyright: ignore[reportUnknownArgumentType]

        if isinstance(self.subset, Dict):
            self.subset = Subset(**self.subset)  # pyright: ignore[reportUnknownArgumentType]

        self.data.sort(key=lambda position: position.position)

    @property
    def sorted_by_position(self):
        """Rankings sorted by position."""
        r = self.data[:]
        r.sort(key=lambda position: position.position)
        return r

    @property
    def sorted_by_delta_position(self):
        """Rankings sorted by change of position."""
        r = self.data[:]
        r.sort(reverse=True, key=lambda position: position.deltaPosition)
        return r

    @property
    def sorted_by_ree(self):
        """Rankings sorted by Ree score."""
        r = self.data[:]
        r.sort(reverse=True, key=lambda position: position.ree)
        return r

    @property
    def sorted_by_delta_ree(self):
        """Rankings sorted by change of Ree score."""
        r = self.data[:]
        r.sort(reverse=True, key=lambda position: position.deltaRee)
        return r
