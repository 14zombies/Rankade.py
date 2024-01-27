# rankade.models.Quota.py
from dataclasses import dataclass

from .Base import RankadeObject


@dataclass(kw_only=True, slots=True)
class Quota(RankadeObject):
    """
    Rankade Quota usage. All items returned as a percentage of total used.
    :::{seealso}
    Quota limits depend on the subscription tier full list can be found on the [Quota and limits](https://rankade.com/api/#quota-and-limits) section of the Rankade API page.
    """

    callsPerYear: str
    """API calls per year"""
    callsPerHour: str
    """API calls per hour"""
    matchesPerYear: str
    """Matches per year"""
    matchesPerDay: str
    """Matches per day"""
    matchesPerHour: str
    """Matches per hour"""
    rankingCallsPerYear: str
    """Ranking calls per year"""
    rankingCallsPerDay: str
    """Ranking calls per day"""
    rankingCallsPerHour: str
    """Ranking calls per hour"""
    apiCreatedGames: str
    """New API-created games"""
