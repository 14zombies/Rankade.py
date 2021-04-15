# Error.py

from dataclasses import InitVar, dataclass, field
from typing import Any, Dict, List, NoReturn, Optional

from rankade import RankadeExceptions

from .Base import RankadeObject, ResultList


@dataclass
class Error(RankadeObject):
    """Represents a single error returned by the Rankade API.
        List of codes & messages returned is here:
         - https://rankade.com/api/#error-responses
         - https://rankade.com/api/#quota-and-limits
         - https://rankade.com/api/#get-auth
         - https://rankade.com/api/#post-players-player
         - https://rankade.com/api/#post-matches-match

    Parameters
    ----------
    _api : :class:`Api`
        Api client.
    message : :class:`str`
        Error message returned by the server.
    code : :class:`str`
        Error code of returned error.


    Atributes
    ----------
    code : :class:`str`
        Error code in returned error.
        If first character is:
            - A – Auth
            - Q – Quota
            - M - Match Validation

    message : :class:`str`
        Error message returned by the server.
    """
    message: str
    code: str


@dataclass
class Errors(ResultList):

    """Represents the error object returned by the Rankade
    server.
    Error object has an array of errors.

    Parameters
    ----------
    api : :class:`Api`
        Api client.
    url : :class:`str`
        Queried url that provided the error response.
    verb : :class:`str`
        HTTP method used in query (GET, POST, etc)
    status : :class:`int`
        HTTP status code returned with the error response.
    data : :class:`List[Dict[str, Any]]`
        List of errors returned in json dict.


    Notes
    -----
    - I have only ever received a single error.
    As the spec is ambiguous this class caters for more than one error.
    """

    url: str
    verb: str
    status: int
    errors: InitVar[Optional[Dict[str, Any]]]  # type: ignore
    _content_class: Any = field(init=False, default=Error)
    data: Any = field(default=None, init=False)

    def __post_init__(self, errors):
        return super().__post_init__(errors)

    def should_raise(self) -> Optional[RankadeExceptions.ApiErrorResponse]:
        """Raises appropriate Exception from each Error recieved from server.

        Raises
        ------
        ApiErrorResponse & subclasses.

        See Also
        --------
        :class:`rankade.RankadeExceptions`
            Full explination of each Exception.
        """
        for error in self.data:
            exception_type = RankadeExceptions.ApiErrorResponse

            if self.status == 202 and error.code[0] == "M":
                exception_type = RankadeExceptions.MatchValidation
            elif self.status == 401 or error.code == "A001":
                exception_type = RankadeExceptions.AuthCredentials
            elif self.status == 429 or (self.status == 202
                                        and error.code[0] == "Q"):
                exception_type = RankadeExceptions.Quotas
            return exception_type(
                self.verb,
                self.url,
                self.status,
                error.code,
                error.message
            )
