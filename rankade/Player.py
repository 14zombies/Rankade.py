# Player.py

import rankade.RankadeObject


class Player(rankade.RankadeObject.RankadeObject):

    def _set_attributes(self, attributes):
        self.id = attributes.get("id")
        self.ghost = attributes.get("ghost")
        self.username = attributes.get("username")
        self.displayName = attributes.get("displayName")
        self.icon = attributes.get("icon")

    @property
    def is_ghost(self):
        return bool(self.ghost)
