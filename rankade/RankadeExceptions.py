# RankadeExceptions.py

class RankadeException(Exception):
    """
        Base Exception, should not be raised directly.
    """
    def __init__(self, message):
        self.message = message


class NoValidCredentials(RankadeException):
    """
        Raised when either no key & secret or no token has been supplied
        to main Rankade class.
        Rasied from:
            - Api.__init__()
            - Api._credentials_params
    """
    def __init__(self, message="No Credentials Supplied"):
        super().__init__(message)


class ApiErrorResponse(RankadeException):
    """
        Base class for error response from API.
        Raised when no appropriate ApiErrorResponse subclass.
        Raised from:
            - Errors.should_raise()
    """
    def __init__(self, url, verb, status, code="", message=""):
        self.url = url
        self.verb = verb
        self.status = status
        self.code = code
        super().__init__(message)


class AuthCredentials(ApiErrorResponse):
    """
        Code will be "A001", raised when key and/or secret are
        invalid or access has been disabled.
        Raised from:
            - Errors.should_raise()
    """
    pass


class Quotas(ApiErrorResponse):
    """
        Code will begin with "Q" and message will contain
        details of the quota limit reached. Status should be either 429 or 202.
        Raised from:
            - Errors.should_raise()
    """
    pass


class MatchValidation(ApiErrorResponse):
    """
        Code will begin with "M" and message will contain
        contain details of validation error with the match.
        Raised from:
            - Errors.should_raise()
    """
    pass


class SearchTooShort(RankadeException):
    """
        Raised when search term is less than 2 characters.
        API will return missing or invalid paramaters which is not useful.
        Raised from:
            - Rankade.game_search()
    """
    def __init__(self, search: str = ""):
        self.search = search
        super().__init__("Search must be at least 2 characters.")
