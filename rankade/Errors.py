# Errors.py

import rankade.Error
import rankade.ResultList

from . import RankadeExceptions


class Errors(rankade.ResultList.ResultList):

    """Represents the error object returned by the Rankade
    server.
    Error object has an array of errors.

    Parameters
    ----------
    url : str
        Queried url that provided the error response.
    verb : str
        HTTP method used in query (GET, POST, etc)
    status : int
        HTTP status code returned with the error response.

    Attributes
    ----------
    contents : [Error]
        Individual error objects returned by the server.
    """

    # Note: I have only ever received a single error.
    # As the spec is ambiguous this class should work for more than one error.

    def __init__(self, api, attributes, url, verb, status):
        super().__init__(api, rankade.Error.Error, attributes)
        self.url = url
        self.verb = verb
        self.status = status

    def should_raise(self):
        """Raises appropriate Exception from each Error recieved from server.
        Raises
        ------
        ApiErrorResponse & subclasses.

        See Also
        --------
        rankade.RankadeExceptions : Full explination of each Exception.
        """
        for error in self.content:
            exception_type = RankadeExceptions.ApiErrorResponse

            if self.status == 202 and error.code[1] == "M":
                exception_type = RankadeExceptions.MatchValidation
            elif self.status == 401 and error.code == "A001":
                exception_type = RankadeExceptions.AuthCredentials
            elif self.status == 429 or (self.status == 202 and error.code[1] == "Q"):
                exception_type = RankadeExceptions.Quotas
            raise exception_type(
                self.verb,
                self.url,
                self.status,
                error.code,
                error.message
            )
