# rankade.models.Error.py
from dataclasses import dataclass, field
from typing import ClassVar, Type

from .Base import RankadeObject, ResultList


@dataclass(kw_only=True, slots=True)
class Error(RankadeObject):
    """
    Represents a single error returned by the Rankade API.

    :::{seealso}
    List of codes & messages returned can be found in the Rankade API documentation.
        - [Error Responses](https://rankade.com/api/#error-responses)
        - [Quota and Limits](https://rankade.com/api/#quota-and-limits)
        - [Get Auth](https://rankade.com/api/#get-auth)
        - [Post Players Player](https://rankade.com/api/#post-players-player)
        - [Post Matched Match](https://rankade.com/api/#post-matches-match)
    :::

    :param str message: Error message returned by the server.
    :param str code: Error code of returned error.

    """

    code: str
    """Error code in returned error.
        If first character will tell you what type of error it is:
            - A: Auth
            - Q: Quota
            - M: Match Validation
    """
    message: str
    """Error message returned by the server."""


@dataclass(kw_only=True, slots=True)
class Errors(ResultList[Error]):

    """
    Represents a list of error objects returned by the Rankade server.
    Individual error objects returned by the server can be accessed in the same way as a regular list.

    :param str url: Queried URL that provided the error response.
    :param str verb: HTTP method used in query (GET, POST, etc)
    :param int status: HTTP status code returned with the error response.
    :param MutableMapping[str, Any] data: List of errors returned in json dict.


    :::{note}
    I have only ever received a single error.
    As the spec is ambiguous this class caters for more than one error.
    :::

    """

    _content_class: ClassVar[Type[RankadeObject]] = Error

    url: str = field(default="")
    """Queried url that provided the error response."""
    verb: str = field(default="")
    """HTTP method used in query (GET, POST, etc)"""
    status: int = field(default=0)
    """HTTP status code returned with the error response."""
