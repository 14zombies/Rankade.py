# Players.py

import rankade.Page
import rankade.Player


class Players(rankade.Page.Page):

    def __init__(self, api, attributes):
        super().__init__(api, rankade.Player.Player, attributes)

    def _set_attributes(self, attributes):
        super()._set_attributes(attributes)
        self._totalPlayers = attributes.get("totalPlayers")

    @property
    def totalPlayers(self):
        return self._totalPlayers

    @property
    def endpoint(self):
        return "players"
