# Ranking.py

import rankade.Player
import rankade.RankadeObject


class Ranking(rankade.RankadeObject.RankadeObject):

    def _set_attributes(self, attributes):

        self.player = rankade.Player.Player(
            self._api, attributes.get("player"))
        self.ree = attributes.get("ree")
        self.deltaRee = attributes.get("deltaRee")
        self.position = attributes.get("position")
        self.deltaPosition = attributes.get("deltaPosition")
        self.belt = attributes.get("belt")
        self.beltLabel = attributes.get("beltLabel")
        self.title = attributes.get("title")
        self.titleLabel = attributes.get("titleLabel")
        self.status = attributes.get("status")
        self.statusLabel = attributes.get("statusLabel")
