# Errors.py

from typing import Any, Dict

import rankade.Api
import rankade.Error
import rankade.ResultList

from . import RankadeExceptions


class Errors(rankade.ResultList.ResultList):

    def __init__(self, api: rankade.Api.Api, attributes: Dict[str, Any], url: str, verb: str, status: int) -> None: ...
    def should_raise(self) -> None: ...
