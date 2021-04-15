# Quota.py
from dataclasses import InitVar, dataclass, field

from .Base import RankadeObject


@dataclass
class Quota(RankadeObject):

    callsPerYear: str
    callsPerHour: str
    matchesPerYear: str
    matchesPerDay: str
    matchesPerHour: str
    rankingCallsPerYear: str
    rankingCallsPerDay: str
    rankingCallsPerHour: str
    apiCreatedGames: str
