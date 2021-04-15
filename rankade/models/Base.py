# Base.py

from dataclasses import InitVar, dataclass, field
from typing import Any, List, Optional, Type
from collections import UserList


@dataclass
class RankadeObject(object):
    """Base class for all objects returned from the server.
    All models should inherit from this class.
    Parameters
    ----------
    _api : :class:`Api`
        Api client.
    """
    _api: Optional["Api"] = field(repr=False, compare=False)  # type: ignore


@dataclass
class ResultList(RankadeObject, UserList):
    """Base class for lists of items from server.

    Parameters
    ---------
    _api : :class:`Api`
        Api client.
    _content_class : :class:`Type`
        List type.
    data : :class:`List[Dict[str, Any]]`
        List of items.

    Attributes
    ----------
    _content_class : :class:`Type`
        List type.
    data : :class:`List[_content_class]`
        List of objects returned by the sever.
    """
    _content_class: Type
    data: list[RankadeObject] = field(default_factory=list, init=False, repr=False, compare=False)  # type: ignore
    data: InitVar[Optional[Any]] = field(repr=False, compare=False, hash=False)

    def __post_init__(self, data):
        typed = []
        if data is None:
            self.data = []
            return
        for item in data:
            if isinstance(item, dict):
                typed.append(self._content_class(self._api, **item))
            elif isinstance(item, self._content_class):
                typed.append(item)
        self.data = typed[:]


@dataclass
class Page(ResultList):
    """Base class for page of items from server .

    Parameters
    ---------
    _api : :class:`Api`
        Api client.
    _content_class : :class:`Type`
        List type.
    data : :class:`List[Dict[str, Any]]`
        List of errors returned in json dict.
    page : :class:`int`
        Current page number.
    totalPages : :class:`int`
        Total Pages.
    rowsForPage : :class:`int`
        Max number of items on page.

    Attributes
    ----------
    _content_class : :class:`Type`
        List type.
    data : :class:`List[_content_class]`
        List of objects returned by the sever.
    page : :class:`int`
        Current page number.
    totalPages : :class:`int`
        Total Pages.
    rowsForPage : :class:`int`
        Max number of items on page.
    """
    page: InitVar[int]
    totalPages: InitVar[int]
    rowsForPage: InitVar[int]


    def __post_init__(self, data, *args):
        super().__post_init__(data)
