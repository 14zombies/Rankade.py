"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, Optional, Type

from .Base import RankadeObject, ResultList
from .Error import Errors

"""
This type stub file was generated by pyright.
"""
@dataclass(kw_only=True, slots=True)
class MatchStatus(RankadeObject):
    """Retrieves API-recorded matches status. [Details](https://rankade.com/api/#get-matches-status)

    :::{note}
    Counts are only for matches entered via API.
    Matches entered via webapp/app are not included.
    :::
    """
    added: int
    processed: int
    queued: int
    total: int
    waiting: int
    ...


@dataclass(kw_only=True, slots=True)
class NewMatchReturn(RankadeObject):
    """Individual match status item returned upon submit."""
    index: int
    id: str
    name: str
    errors: Optional[Errors] = ...
    def __post_init__(self) -> None:
        ...



@dataclass(kw_only=True, slots=True)
class NewMatchReturnList(ResultList[NewMatchReturn]):
    """lists "accepted & rejected" from NewMAtchResponse are NewMatchReturnList objects."""
    _content_class: ClassVar[Type[RankadeObject]] = ...


@dataclass(kw_only=True, slots=True)
class NewMatchResponse(RankadeObject):
    """Response from the server to a posted Match."""
    total: int
    acceptedCount: int
    rejectedCount: int
    rejected: NewMatchReturnList
    accepted: NewMatchReturnList
    dryrun: bool
    def __init__(self, total: int, acceptedCount: int, rejectedCount: int, rejected: Dict[str, Any], accepted: Dict[str, Any], dryrun: bool = ...) -> None:
        """
        :param int total: Total matches submitted.
        :param int acceptedCount: Total matches accepted.
        :param int rejectedCount: Total matches rejected.
        :param Dict[str, Any] rejected: List of rejected matches with errors.
        :param Dict[str, Any] accepted: List of accepted matches.
        :param bool dryrun: Reports True if posting was a test and not actually submitted.
        """
        ...

    @property
    def has_error(self) -> bool:
        """Convenience method returns True if any submitted matches are rejected."""
        ...



