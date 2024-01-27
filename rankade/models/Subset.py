# rankade.models.Subset.py
from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, Optional, Type

from .Base import RankadeObject, ResultList
from .Game import Game
from .Match import Match, Matches


@dataclass(kw_only=True, slots=True)
class Subset(RankadeObject):
    """Represents a groups subset."""

    id: str
    """Subset id."""
    name: str
    """Subset name."""
    type: str
    """Subset type."""
    creationDate: datetime
    """Subset creation date."""
    isMain: bool
    """Subset is the main subset."""
    isCustom: bool
    """Subset is a custom subset."""
    icon: str
    """Subset icon URL."""
    countMatches: int
    """Total matches in subset."""
    game: Optional[Game]
    """Game associated with the subset."""
    firstMatch: Match
    """First match included in the subset."""
    lastMatch: Match
    """Last match included in the subset."""

    def __post_init__(self):
        if isinstance(self.isMain, int):  # pyright: ignore[reportUnnecessaryIsInstance]
            self.isMain = bool(self.isMain)
        if isinstance(self.isCustom, int):  # pyright: ignore[reportUnnecessaryIsInstance]
            self.isCustom = bool(self.isCustom)
        if isinstance(self.creationDate, str):
            self.creationDate = datetime.fromisoformat(self.creationDate)
        if isinstance(self.game, dict):
            self.game = Game(**self.game)  # pyright: ignore[reportUnknownArgumentType]

        if isinstance(self.firstMatch, dict):
            self.firstMatch = Match(**self.firstMatch)  # pyright: ignore[reportUnknownArgumentType]

        if isinstance(self.lastMatch, dict):
            self.lastMatch = Match(**self.lastMatch)  # pyright: ignore[reportUnknownArgumentType]

    @property
    def matches(self):
        """Includes bot the first and last match in the subset."""
        return Matches(data=[self.firstMatch, self.lastMatch], totalMatches=2)


@dataclass(kw_only=True, slots=True)
class Subsets(ResultList[Subset]):
    """
    Represents the list of subsets returned by the Rankade server.
    Individual subset objects returned by the server can be accessed in the same way as a regular list.
    """

    _content_class: ClassVar[Type[RankadeObject]] = Subset
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""
