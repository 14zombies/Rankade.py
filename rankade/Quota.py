# Quota.py
import rankade.RankadeObject


class Quota(rankade.RankadeObject.RankadeObject):

    def _set_attributes(self, attributes):
        self.callsPerYear = attributes.get("callsPerYear")
        self.matchesPerYear = attributes.get("callsPerHour")
        self.matchesPerYear = attributes.get("matchesPerYear")
        self.matchesPerDay = attributes.get("matchesPerDay")
        self.matchesPerHour = attributes.get("matchesPerHour")
        self.rankingCallsPerYear = attributes.get("rankingCallsPerYear")
        self.rankingCallsPerDay = attributes.get("rankingCallsPerDay")
        self.rankingCallsPerHour = attributes.get("rankingCallsPerHour")
        self.apiCreatedGames = attributes.get("apiCreatedGames")
