# Games.py

import rankade.Game
import rankade.ResultList


class Games(rankade.ResultList.ResultList):
    """Represents the list of Games returned by the Rankade
    server.

    Attributes
    ----------
    contents : [Error]
        Individual game objects returned by the server.
    """

    def __init__(self, api, attributes):
        super().__init__(api, rankade.Game.Game, attributes)
