# Page.py

import rankade.Player
import rankade.ResultList

from typing import Any, Dict, Optional


class Page(rankade.ResultList.ResultList):

    def _set_attributes(self, attributes: Dict[str, Any]) -> None: ...

    async def next_page(self) -> Optional[Page]: ...
