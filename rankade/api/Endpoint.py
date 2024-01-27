# rankade.api.Endpoint.py
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING, MutableMapping, Optional, Union

from enum_tools.documentation import document_enum

if TYPE_CHECKING:
    from .Api import HEADERS, JSON, PARAMS


class Endpoint_Method(Enum):
    """HTTP Request methods [RFC2616 Section 5.1.1](https://www.rfc-editor.org/rfc/rfc2616#section-5.1.1)"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    CONNECT = "CONNECT"


@dataclass
class Endpoint_Mixin:
    """Stores the basic information needed for each endpoint."""

    auth: bool
    """Does the request need authorisation before proceeding."""
    paginated: bool
    """Will the response be paginated."""
    method: Endpoint_Method
    """HTTP Method used in the request."""
    base_path: str
    """URL path to use in request."""


@document_enum
class Endpoint(Endpoint_Mixin, Enum):
    """
    Enum with information needed for each request.
    auth, paginated, method, base_path
    """

    AUTH = False, False, Endpoint_Method.GET, "auth"
    """
    Authorisation returns JWT. [GET /auth](https://rankade.com/api/#get-auth)
    """
    GAME = True, False, Endpoint_Method.POST, "games/game"
    """
    Creates a new game by giving its bggId (BoardGameGeek game id) or a game name. [POST /games/game](https://rankade.com/api/#post-games-game)
    """
    GAMES = True, False, Endpoint_Method.GET, "games"
    """
    Returns the list of the group's games (i.e. games with at least one match played within the group). [GET /games](https://rankade.com/api/#get-games)
    """
    GAMES_POPULAR = True, False, Endpoint_Method.GET, "games/popular"
    """
    Returns the list of rankade's most popular games. [GET /games/popular](https://rankade.com/api/#get-games-popular)
    """
    GAMES_SEARCH = True, False, Endpoint_Method.GET, "games/search"
    """
    Searches games by name. [GET /games/search](https://rankade.com/api/#get-games-search)
    """
    MATCH = True, False, Endpoint_Method.POST, "matches/match"
    """
    Adds one or more matches to the group. [POST /matches/match](https://rankade.com/api/#post-matches-match)
    """
    MATCH_EXISTS = True, False, Endpoint_Method.GET, "matches/match/exists"
    """
    Check if an accepted match exists by giving its external identifier. [GET /matches/match/exists](https://rankade.com/api/#get-matches-match-exists)
    """
    MATCH_STATUS = True, False, Endpoint_Method.GET, "matches/status"
    """
    Retrieves API-recorded matches status. [GET /matches/status](https://rankade.com/api/#get-matches-status)
    """
    MATCHES = True, True, Endpoint_Method.GET, "matches{subset}{page}"
    """
    Retrieve registered and processed matches. [GET /matches](https://rankade.com/api/#get-matches)
    """
    PLAYER = True, False, Endpoint_Method.POST, "players/player"
    """
    Create a ghost player within the group.[POST /players/player](https://rankade.com/api/#post-players-player)
    """
    PLAYERS = True, True, Endpoint_Method.GET, "players{page}"
    """
    Returns the list of the group's players. [GET /player](https://rankade.com/api/#get-players)
    """
    QUOTA = True, False, Endpoint_Method.GET, "quota"
    """
    Returns quota usage details in percentage for the current client. [GET /quota] (https://rankade.com/api/#get-quota)
    """
    RANKINGS = True, True, Endpoint_Method.GET, "rankings{subset}{match}{page}"
    """
    Get a groups rankings, filter by subset, beginning with match number. [GET /rankings](https://rankade.com/api/#get-rankings)
    """
    STATUS = True, False, Endpoint_Method.GET, "status"
    """
    Returns the status of the service. [GET /status](https://rankade.com/api/#get-status)
    """
    SUBSET = True, False, Endpoint_Method.GET, "subset"
    """
    Returns a list of the groups subsets. [GET /subsets](https://rankade.com/api/#get-subsets)
    """
    _TEST = False, False, Endpoint_Method.GET, "test"
    """
    Endpoint used for unit tests.
    """


@dataclass
class Endpoint_Request:
    """Full information needed for Api.request to make a request."""

    endpoint: Endpoint
    """Basic information for Endpoint"""
    params: PARAMS = field(default=None)
    """Additional Parameters to be used in request"""
    headers: HEADERS = field(default=None)
    """Additional Headers to be used in the request"""
    json: JSON = field(default=None)
    """JSON to be sent as part of the request"""
    page: Optional[int] = field(init=False, default=None)
    """Page number to be requested"""
    match: Optional[int] = field(default=None)
    """Match number to be requested"""
    subset: Optional[str] = field(default=None)
    """Subset Id to be requested"""

    def __post_init__(self):
        if self.endpoint.paginated:
            self.page = 1

    @property
    def path(self) -> str:
        """Builds the URL path to use, from the base path included in the Endpoint with {page}, {match}, & {subset} replaced with the appropriate value"""
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
        return self.endpoint.base_path.format(subset=subset_str, match=match_str, page=page_str)

    @property
    def method(self) -> str:
        """Returns the required HTTP method to be used for the endpoint."""
        return self.endpoint.method.value

    @property
    def requires_auth(self) -> bool:
        """Does the endpoint require authorisation before making the request."""
        return self.endpoint.auth

    @property
    def is_paginated(self) -> bool:
        """Will the request return a paginated response."""
        return self.endpoint.paginated

    def add_parameter(self, name: str, value: str) -> MutableMapping[str, Union[str, int]]:
        """Convenience method to add a custom parameter."""
        if self.params is None:
            self.params = {}
        self.params[name] = value
        return self.params

    def add_header(self, name: str, value: str) -> MutableMapping[str, str]:
        """Convenience method to add a custom header."""
        if self.headers is None:
            self.headers = {}
        self.headers[name] = value
        return self.headers

    def set_json(self, json: JSON) -> JSON:
        """Convenience method to set the JSON body of the request."""
        if self.json is None:
            self.json = {}
        self.json = json
        return self.json
