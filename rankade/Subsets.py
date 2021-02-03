# Subsets.py

import rankade.ResultList
import rankade.Subset


class Subsets(rankade.ResultList.ResultList):

    def __init__(self, api, attributes):
        super().__init__(api, rankade.Subset.Subset, attributes)
