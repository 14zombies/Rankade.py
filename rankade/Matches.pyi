# Matches.py

from typing import Any, Dict

import rankade.Api
import rankade.Match
import rankade.Page


class Matches(rankade.Page.Page):

    def __init__(self, api: rankade.Api.Api,
                 attributes: Dict[str, Any]) -> None: ...

    def _set_attributes(self, attributes: Dict[str, Any]) -> None: ...

    @property
    def endpoint(self): ...
