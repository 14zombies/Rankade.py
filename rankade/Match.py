# Match.py

import json

import rankade.Faction
import rankade.Game
import rankade.Player
import rankade.RankadeObject


class Match(rankade.RankadeObject.RankadeObject):

    def _set_attributes(self, attributes):
        self.id = attributes.get("id")
        self.externalId = attributes.get("externalId")
        self.date = attributes.get("date")
        self.registrationDate = attributes.get("registrationDate")
        self.number = attributes.get("number")
        self.summary = attributes.get("summary")
        self.matchType = attributes.get("type")
        self.draw = attributes.get("draw")
        self.weight = attributes.get("weight")
        self.weightLabel = attributes.get("weightLabel")
        self.game = rankade.Game.Game(self._api, attributes.get("game"))
        self.factions = []
        if attributes.get("factions") is not None:
            for faction in attributes.get("factions"):
                self.factions.append(
                    rankade.Faction.Faction(self._api, faction))
        self.notes = attributes.get("notes")

    @property
    def is_draw(self):
        return bool(self.draw)

    @property
    def winning_factions(self):
        return [faction for faction in self.factions if faction.rank == 1]

    @property
    def winning_players(self):
        faction_players = [
            faction.players for faction in self.winning_factions]
        return [player for faction in faction_players for player in faction]

    def add_faction(self, players, rank, points):
        # if not isinstance(players, [rankade.Player.Player]):
        #     raise Exception
        if not isinstance(rank, int):
            raise Exception
        if not isinstance(points, str):
            raise Exception
        if len(players) < 1:
            raise Exception
        players_dict = []
        for player in players:
            if player.id == "bot" and len(players) > 1:
                #A bot faction cannot contain any players.
                Exception

            players_dict.append(player.__dict__)
        attributes = {
            "players": players_dict,
            "rank": rank,
            "points": points
        }
        faction = rankade.Faction.Faction(self._api, attributes)
        self.factions.append(faction)

    def add_bot_faction(self, rank, points):
        bot_attributes = {
            "id": "bot"
        }
        bot_player = rankade.Player.Player(self._api, bot_attributes)
        self.add_faction(bot_player, rank, points)

    async def save(self):
        if self.id is None:
            await self._api.post("matches/match", json=self.to_json())
        else:
            # Cannot edit matches.
            Exception

    def to_json(self):
        json_factions = []
        for faction in self.factions:
            json_factions.append(faction.to_json())
        match = [{
            "game": self.game.id,
            "weight": self.game.weight,
            "factions": json_factions,
            "notes": self.notes
        }]
        return match
