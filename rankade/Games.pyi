# Games.py

from typing import Any, Dict

import rankade.Api
import rankade.Game
import rankade.ResultList


class Games(rankade.ResultList.ResultList):

    def __init__(self, api: rankade.Api.Api,
                 attributes: Dict[str, Any]) -> None: ...
