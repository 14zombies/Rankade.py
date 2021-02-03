# Matches.py

import rankade.Match
import rankade.Page


class Matches(rankade.Page.Page):

    """Represents the a Matches page, returned by Rankade API.

    Attributes
    ----------
    contents : [Match]
        Individual Match objects returned by the server.
    page : int
        Page number.
    rowsForPage : int
        Max number of Match objects per page.
    totalMatches : int
        Total matches on all pages.
    totalPages : int
        Total number of pages.
    endpoint : str
        Main rankade api endpoint.

    Methods
    -------
    next_page
        Returns the next page or None if last page.
    """

    def __init__(self, api, attributes):
        super().__init__(api, rankade.Match.Match, attributes)

    def _set_attributes(self, attributes):
        super()._set_attributes(attributes)
        self.totalMatches = attributes.get("totalMatches")

    @property
    def endpoint(self):
        return "matches"
