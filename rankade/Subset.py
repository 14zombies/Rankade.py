# Subset.py

import rankade.Game
import rankade.Match
import rankade.RankadeObject


class Subset(rankade.RankadeObject.RankadeObject):

    def _set_attributes(self, attributes):
        self.id = attributes.get("id")
        self.name = attributes.get("name")
        self.type = attributes.get("type")
        self.createionDate = attributes.get("creationDate")
        self.isMain = attributes.get("isMain")
        self.isCustom = attributes.get("isCustom")
        self.icon = attributes.get("icon")
        self.game = None
        if attributes.get("game") is not None:
            game_attributes = attributes.get("game")
            self.game = rankade.Game.Game(self._api, game_attributes)
        self.countMatches = attributes.get("countMatches")
        self.firstMatch = None
        if attributes.get("firstMatch") is not None:
            self.firstMatch = rankade.Match.Match(
                self._api, attributes.get("firstMatch"))
        self.lastMatch = None
        if attributes.get("lastMatch") is not None:
            self.lastMatch = rankade.Match.Match(
                self._api, attributes.get("lastMatch"))
