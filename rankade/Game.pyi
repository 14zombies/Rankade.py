# Game.py

from typing import Any, Dict

import rankade.RankadeObject


class Game(rankade.RankadeObject.RankadeObject):

    def _set_attributes(self, attributes: Dict[str, Any]) -> None: ...
