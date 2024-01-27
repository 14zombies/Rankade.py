# rankade.RankadeExceptions.py
class RankadeException(Exception):
    """
    Base Exception, should not be raised directly.
    """

    def __init__(self, message: str):
        self.message = message


class ApiErrorResponse(RankadeException):
    """
    Base class for error response from API.
    Raised when no appropriate ApiErrorResponse subclass.

    Raised from:
    - {py:meth}`rankade.api.Api.Api._check_request`

    :param str url: URL queried.
    :param str verb: HTTP Method used.
    :param str status: Request HTTP status code.
    :param str code: API error code.
    :param str message: API error message.
    """

    def __init__(self, url: str, verb: str, status: int, code: str = "", message: str = ""):
        self.url = url
        self.verb = verb
        self.status = status
        self.code = code
        super().__init__(message)


class AuthCredentials(ApiErrorResponse):
    """
    Code will be "A001" or "A002", raised when key and/or secret are
    invalid or access has been disabled.

    Raised from:
    - {py:meth}`rankade.api.Api.Api._check_request`
    """

    pass


class MatchValidation(ApiErrorResponse):
    """
    Code will begin with "M" and message will contain
    contain details of validation error with the match.

    Raised from:
    - {py:meth}`rankade.api.Api.Api._check_request`
    """

    pass


class NoValidCredentials(RankadeException):
    """
    Raised when either no key & secret or no token has been supplied
    to main Rankade class.

    Raised from:
    - {py:class}`rankade.api.Api.Api`
    - {py:meth}`rankade.api.Api.Api._request_jwt`
    """

    def __init__(self, message: str = "No Credentials Supplied"):
        super().__init__(message)


class Quotas(ApiErrorResponse):
    """
    Code will begin with "Q" and message will contain
    details of the quota limit reached. Status should be either 429 or 202.

    Raised from:
    - {py:meth}`rankade.api.Api.Api._check_request`
    """

    pass


class SearchTooShort(RankadeException):
    """
    Raised when search term is less than 2 characters.
    API will return missing or invalid parameters which is not useful.

    Raised from:
    - {py:meth}`rankade.Rankade.Rankade.game_search`
    """

    def __init__(self, search: str = ""):
        self.search = search
        super().__init__(f"Search must be at least 2 characters (got '{search}').")
