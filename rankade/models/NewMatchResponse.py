# rankade.models.NewMatchResponse.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional, Type

from .Base import RankadeObject, ResultList
from .Error import Errors

"""
NewMatchResponse is the object that comes back from the server. It will contain 2 lists "accepted & rejected" which are NewMatchReturnList objects.
The NewMatchReturnList objects are lists of NewMatchReturn.

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
    """Matches added to subset(s), both processed and not yet processed."""
    processed: int
    """Processed matches."""
    queued: int
    """Accepted matches, queued for insertion."""
    total: int
    """Total API-recorded matches."""
    waiting: int
    """Inserted matches, waiting for their subset(s)."""


@dataclass(kw_only=True, slots=True)
class NewMatchReturn(RankadeObject):
    """Individual match status item returned upon submit."""

    index: int
    """Match index."""
    id: str
    """Match Id."""
    name: str
    """Match name."""
    errors: Optional[Errors] = None
    """List of errors in match, if appropriate."""

    def __post_init__(self):
        if isinstance(self.errors, List):
            self.errors = Errors.from_dict(data_dict=self.errors)  # pyright: ignore[reportArgumentType]


@dataclass(kw_only=True, slots=True)
class NewMatchReturnList(ResultList[NewMatchReturn]):
    """lists "accepted & rejected" from NewMAtchResponse are NewMatchReturnList objects."""

    _content_class: ClassVar[Type[RankadeObject]] = NewMatchReturn
    """Classvar to allow the an object in the list to be created from a dict returned from the server."""


@dataclass(kw_only=True, slots=True)
class NewMatchResponse(RankadeObject):
    """Response from the server to a posted Match."""

    total: int
    """Total matches submitted."""
    acceptedCount: int
    """Total matches accepted."""
    rejectedCount: int
    """Total matches rejected."""
    rejected: NewMatchReturnList
    """List of rejected matches with errors."""
    accepted: NewMatchReturnList
    """List of accepted matches."""

    def __init__(
        self,
        total: int,
        acceptedCount: int,
        rejectedCount: int,
        rejected: Dict[str, Any],
        accepted: Dict[str, Any],
    ):
        """
        :param int total: Total matches submitted.
        :param int acceptedCount: Total matches accepted.
        :param int rejectedCount: Total matches rejected.
        :param Dict[str, Any] rejected: List of rejected matches with errors.
        :param Dict[str, Any] accepted: List of accepted matches.
        """
        self.total = total
        self.acceptedCount = acceptedCount
        self.rejectedCount = rejectedCount

        self.rejected = NewMatchReturnList.from_dict(data_dict=rejected)
        self.accepted = NewMatchReturnList.from_dict(data_dict=accepted)

    @property
    def has_error(self) -> bool:
        """Convenience method returns True if any submitted matches are rejected."""
        return len(self.rejected) > 0
