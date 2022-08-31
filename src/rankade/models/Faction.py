# Faction.py
import json
from dataclasses import InitVar, dataclass, field
from typing import Any, Dict, List, Optional

from .Player import Player
from .Base import RankadeObject


@dataclass
class Faction(RankadeObject):
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

    points: str
    rank: int
    players: InitVar[List]  # type: ignore
    name: Optional[str] = None
    bot: Optional[int] = None
    winner: Optional[int] = None
    _players: List[Player] = field(
        default_factory=list, init=False)
    countPlayers: Optional[int] = 0

    def __post_init__(self, players):
        for player in players:
            self._players.append(Player(**player))

    @property
    def players(self) -> List[Player]:
        return self._players

    @property
    def is_bot(self):
        if self.bot is not None:
            return bool(self.bot)
        else:
            return self.players[0].id == "bot"

    def to_json(self):
        """Returns json for server post request.
        """
        ids = [str(p) for p in self._players]
        faction_json = {"rank": int(self.rank),
                        "score": str(self.points), "players": ids}
        return faction_json
