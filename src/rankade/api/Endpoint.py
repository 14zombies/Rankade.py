# Endpoint.py

from dataclasses import InitVar, dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


@dataclass
class Endpoint_Request:

    auth: InitVar[bool]  # type: ignore
    paginated: InitVar[bool]  # type: ignore
    method: InitVar[str]  # type: ignore
    path: InitVar[str]  # type: ignore
    params: Dict[str, Any] = field(default_factory=dict)
    headers: Dict[str, Any] = field(default_factory=dict)
    json: Dict[str, Any] = field(default_factory=dict)
    page: Optional[int] = field(init=False, default=None)
    match: Optional[int] = field(init=False, default=None)
    subset: Optional[str] = field(init=False, default=None)

    _auth: bool = field(default=True, init=False)
    _paginated: bool = field(default=False, init=False)
    _method: str = field(default="GET", init=False)
    _path: str = field(default="", init=False)

    def __post_init__(self, auth, paginated, method, path):
        self._auth = auth
        self._paginated = paginated
        self._method = method
        self._path = path
        if paginated:
            self.page = 1

    @property
    def auth(self):
        return self._auth

    @property
    def paginated(self):
        return self._paginated

    @property
    def method(self):
        return self._method

    @property
    def path(self):
        page_str = ""
        subset_str = ""
        if self.page is not None:
            page_str = "/" + str(self.page)
        if self.match is None:
            match_str = "/last"
        else:
            match_str = "/" + str(self.match)
        if self.subset is not None:
            subset_str = "/" + self.subset
        return self._path.format(subset=subset_str, match=match_str, page=page_str)


class Endpoint(Enum):
    AUTH = Endpoint_Request(auth=False, paginated=False,
                            method="GET", path="auth")
    GAMES = Endpoint_Request(auth=True, paginated=False,
                             method="GET", path="games")
    POPULAR_GAMES = Endpoint_Request(
        auth=True, paginated=False, method="GET", path="games/popular")
    SEARCH_GAMES = Endpoint_Request(
        auth=True, paginated=False, method="GET", path="games/search")
    MATCH = Endpoint_Request(auth=True, paginated=False, method="POST", path="matches/match")
    MATCH_EXISTS = Endpoint_Request(
        auth=True, paginated=False, method="GET", path="matches/match/exists")
    MATCH_STATUS = Endpoint_Request(
        auth=True, paginated=False, method="GET", path="matchs/status")
    MATCHES = Endpoint_Request(
        auth=True, paginated=True, method="GET", path="matches{subset}{page}")
    PLAYER = Endpoint_Request(
        auth=True, paginated=False, method="POST", path="players/player")
    PLAYERS = Endpoint_Request(
        auth=True, paginated=True, method="GET", path="players{page}")
    QUOTA = Endpoint_Request(auth=True, paginated=False,
                             method="GET", path="quota")
    STATUS = Endpoint_Request(
        auth=True, paginated=False, method="GET", path="status")
    SUBSET = Endpoint_Request(
        auth=True, paginated=False, method="GET", path="subset")
    RANKINGS = Endpoint_Request(
        auth=True, paginated=True, method="GET", path="rankings{subset}{match}{page}")

    @property
    def path(self):
        return self.value.path

    @property
    def method(self):
        return self.value.method

    @property
    def is_paginated(self):
        return self.value.paginated

    @property
    def requires_auth(self):
        return self.value._auth

    @property
    def params(self):
        return self.value.params

    @property
    def headers(self):
        return self.value.headers

    @property
    def json(self):
        return self.value.json

    @property
    def page(self):
        return self.value.page

    @page.setter
    def page(self, value):
        self.value.page = value

    @property
    def subset(self):
        return self.value.subset

    @subset.setter
    def subset(self, value):
        self.value.subset = value

    def add_paramater(self, name: str, value: str):
        self.value.params[name] = value

    def add_header(self, name: str, value: str):
        self.value.headers[name] = value

    def set_json(self, json):
        self.value.json = json
