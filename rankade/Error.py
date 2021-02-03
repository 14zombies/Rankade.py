# Error.py

import rankade.RankadeObject


class Error(rankade.RankadeObject.RankadeObject):
    """Represents a single error in the errors response object
        (see Errors) returned by Rankade API.
        List of codes & messages returned is here:
         - https://rankade.com/api/#error-responses
         - https://rankade.com/api/#quota-and-limits
         - https://rankade.com/api/#get-auth
         - https://rankade.com/api/#post-players-player
         - https://rankade.com/api/#post-matches-match

    Atributes
    ----------
    code : str
        Error code in returned error object.
        If first character is:
            - A – Auth
            - Q – Quota
            - M - Match Validation

    message: str
        Error message returned by the server.
    """

    def _set_attributes(self, attributes):
        self.code = attributes.get("code")
        self.message = attributes.get("message")
