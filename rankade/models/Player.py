# rankade.models.Player.py
from dataclasses import dataclass, field
from typing import ClassVar, Dict, List, Optional, Type

from ..Consts import GHOST_PREFIX
from .Base import Page, RankadeObject


@dataclass(kw_only=True, slots=True)
class Player(RankadeObject):
    """Represents a single player returned by the Rankade API."""

    id: str
    """Player id"""
    ghost: bool
    """True if player is a ghost"""
    displayName: str
    """Player display name"""
    icon: str
    """Player Icon URL"""
    username: Optional[str] = None
    """Player username, will be None if player is a ghost"""

    def __post_init__(self):
        if isinstance(self.ghost, int):  # pyright: ignore[reportUnnecessaryIsInstance]
            self.ghost = bool(self.ghost)

    @property
    def is_ghost(self):
        """Convenience method returns self.ghost"""
        return self.ghost


@dataclass(kw_only=True, slots=True)
class Players(Page[Player]):
    """
    Represents a list of player objects returned by the Rankade server.
    Individual player objects returned by the server can be accessed in the same way as a regular list.
    """

    totalPlayers: int = field(default=0)
    """Total matches on all pages."""
    _content_class: ClassVar[Type[RankadeObject]] = Player
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""

    @property
    def ids(self) -> List[str]:
        """Player & ghost ids"""
        return [player.id for player in self.data]

    @property
    def ghosts(self) -> List[Player]:
        """All ghost players."""
        return [player for player in self.data if player.is_ghost]

    @property
    def display_names(self) -> List[str]:
        """
        Display names for players & ghosts.
        Ghost display names have a '*' prefix.
        """
        return [player.displayName for player in self.data]

    @property
    def display_names_clean(self) -> List[str]:
        """
        Display names for players & ghosts.
        Ghost display names will be returned without '*' prefix.
        """
        return [player.displayName.replace(GHOST_PREFIX, "") for player in self.data]

    @property
    def usernames(self) -> List[str | None]:
        """Usernames for all players, ghosts not included."""
        x = [player.username for player in self.data if player.username != ""]
        return x

    @property
    def icons(self) -> Dict[str, str]:
        """All icon URIs for players & ghosts (if set.)"""
        ids = [player.id for player in self.data if player.icon != ""]
        icons = [player.icon for player in self.data if player.icon != ""]
        return dict(zip(ids, icons, strict=False))
