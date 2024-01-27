# rankade.models.Base.py
from __future__ import annotations

from abc import ABC
from collections import UserList
from copy import deepcopy
from dataclasses import dataclass, field
from typing import (
    Any,
    ClassVar,
    List,
    MutableMapping,
    MutableSequence,
    Optional,
    Type,
    TypeVar,
    Union,
)

T = TypeVar("T", bound="RankadeObject")


@dataclass(slots=True)
class RankadeObject(ABC):  # noqa: B024

    """
    Base class for all objects returned from the server.
    All models should inherit from this class.
    """

    pass


@dataclass(kw_only=True, slots=True)
class ResultList(UserList[T], RankadeObject):
    """
    Base class for lists of items from server.

    :param List[rankade.models.Base.T] data: List of RankadeObjects returned by the sever.
    """

    _content_class: ClassVar[Type[RankadeObject]]
    """Classvar to be overridden on each subclass to allow the an object in the list to be created from a dict returned from the server."""
    data: List[T]
    """List of RankadeObjects returned by the sever."""

    @classmethod
    def from_dict(cls, data_dict: Union[MutableMapping[str, Any], MutableSequence[MutableMapping[str, Any]]]):
        """
        Create a ResultList instance from a dict.
        """
        content_class = cls._content_class
        if isinstance(data_dict, MutableSequence):
            data_dict = {"data": data_dict}
        data = [content_class(**item) for item in data_dict.get("data", [])]
        # make a copy here as it was modifying the original and screwing up tests!
        copyof_data_dict = deepcopy(data_dict)
        del copyof_data_dict["data"]
        return cls(**copyof_data_dict, data=data)


@dataclass(kw_only=True, slots=True)
class Page(ResultList[T]):
    """
    Base class for page of items from server .

    :param List[rankade.models.Base.T] data: List RankadeObject objects.
    :param int page: Current page number.
    :param int totalPages: Total Pages.
    :param int rowsForPage: Max number of items on page.

    """

    page: int = field(default=1)
    """Page number"""
    totalPages: int = field(default=1)
    """Total pages"""
    rowsForPage: Optional[int] = None
    """How many items the server will return on each page."""
