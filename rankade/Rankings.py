# Rankings.py

import rankade.Ranking
import rankade.Page
import rankade.Match
import rankade.Subset


class Rankings(rankade.Page.Page):

    def __init__(self, api, attributes):
        super().__init__(api, rankade.Ranking.Ranking, attributes)

    def _set_attributes(self, attributes):
        super()._set_attributes(attributes)
        self.match = None
        if attributes.get("match") is not None:
            self.match = rankade.Match.Match(self._api, attributes.get("match"))
        self.subset = None
        if attributes.get("subset") is not None:
            self.subset = rankade.Subset.Subset(self._api, attributes.get("subset"))

    @property
    def endpoint(self):
        return "rankings"
