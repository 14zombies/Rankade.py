# Faction.py

import rankade.Player
import rankade.RankadeObject


class Faction(rankade.RankadeObject.RankadeObject):
    """ Represents a faction used within a Match.
    Attributes
    ----------
    name : str
        Faction Name,
    players : Dict[rankade.Player.Player]
        List of faction players.
    points : str
        Faction points/score,
    rank : int
        Faction ranking compared to other factions.
    winner : int
        Raw data from api 1 is faction is a winner, 0 if not.
        See Also
        --------
        is_winner
    is_winner : bool
        Convenience attribute – returns true if faction is winning faction.
    is_bot : bool
        Convenience attribute – returns true if facion is bot faction.
    """

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def _set_attributes(self, attributes):
        self.bot = attributes.get("bot")
        self.name = attributes.get("name")
        self.players = []
        for player in attributes.get("players"):
            self.players.append(rankade.Player.Player(self._api, player))
        self.points = attributes.get("points")
        self.rank = attributes.get("rank")
        self.winner = attributes.get("winner")

    @property
    def is_bot(self):
        if self.bot is not None:
            return bool(self.bot)
        else:
            return self.players[0].id == "bot"

    def to_json(self):
        """Returns json for server post request.
        """
        ids = []
        for player in self.players:
            ids.append(str(player.id))
        faction_json = {"rank": int(self.rank),
                        "points": str(self.points), "players": ids}
        return faction_json
