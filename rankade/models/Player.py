# Player.py

from dataclasses import dataclass, field, InitVar
from typing import Any, List, Optional

from .Base import RankadeObject
from .Base import Page


@dataclass
class Player(RankadeObject):

    id: str
    ghost: int
    displayName: str
    icon: str
    username: Optional[str] = None

    @property
    def is_ghost(self):
        return bool(self.ghost)


@dataclass()
class Players(Page):
    """List of players and ghosts.
    Accessable using standard list syntax i.e. players[0]

    Attributes
    ----------
    ids : :class:`List[str]`
        Player & ghost ids

    ghosts : :class:`List[Player]`
        All ghost players

    display_names : :class:`List[str]`
        Display names for players & ghosts.
        Ghost display names have a '*' prefix.

    display_names_clean : :class:`List[str]`
        Display names for players & ghosts.
        Ghost display names do not inculde '*' prefix.

    usernames : :class:`List[str]`
        Usernames for all players, ghosts not included.

    icons : :class:`List[str]`
        All icon URIs for players & ghosts (if set.)
    """

    totalPlayers: InitVar[int] = field(default=0)
    _content_class: Any = field(init=False, default=Player)

    def __post_init__(self, data, *args):
        super().__post_init__(data, *args)

    @property
    def ids(self) -> List[str]:
        return [player.id for player in self.data]

    @property
    def ghosts(self) -> List[Player]:
        return [player for player in self.data if player.is_ghost]

    @property
    def display_names(self) -> List[str]:
        return [player.displayName for player in self.data]

    @property
    def display_names_clean(self) -> List[str]:
        return [player.displayName.replace("*", "") for player in self.data]

    @property
    def usernames(self) -> List[str]:
        return [player.username for player in self.data]

    @property
    def icons(self) -> List[str]:
        return [player.icon for player in self.data]
