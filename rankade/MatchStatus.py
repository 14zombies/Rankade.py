# MatchStatus.py

import rankade.RankadeObject


class MatchStatus(rankade.RankadeObject.RankadeObject):
    """Retrieves API-recorded matches status.
    Details: https://rankade.com/api/#get-matches-status

    Attributes
    ----------
    added : int
        Matches added to subset(s), both processed and not yet processed.
    processed : int
        Processed matches.
    queued : int
        Accepted matches, queued for insertion.
    total : int
        Total API-recorded matches.
    waiting : int
        Inserted matches, waiting for their subset(s).

    Notes
    -----
    Counts are only for matches entered via API.
    Matches entered via webapp/app are not included.
    """

    def _set_attributes(self, attributes):
        self.added = attributes.get("added")
        self.processed = attributes.get("processed")
        self.queued = attributes.get("queued")
        self.total = attributes.get("total")
        self.waiting = attributes.get("waiting")
