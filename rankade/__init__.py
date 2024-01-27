# rankade.__init__.py
__title__ = "rankade"
__author__ = "14zombies"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present 14zombies"
__version__ = "0.1.2"

import logging

from rankade import RankadeExceptions
from rankade.models import *
from rankade.Rankade import Rankade

logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = [
    "Rankade",
    "RankadeExceptions",
    "Error",
    "Errors",
    "Faction",
    "Factions",
    "Game",
    "Games",
    "Match",
    "Matches",
    "MatchStatus",
    "NewMatch",
    "NewMatchList",
    "NewMatchResponse",
    "NewMatchReturn",
    "NewMatchReturnList",
    "Player",
    "Players",
    "Quota",
    "RankadeObject",
    "Ranking",
    "Rankings",
    "ResultList",
    "Subset",
    "Subsets",
]
