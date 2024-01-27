import unittest

from rankade import Rankade, models
from rankade.RankadeExceptions import RankadeException

from . import consts


class TestMatchCreation(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        token: str = consts.make_token(consts.valid_token_message)
        self.rankade = Rankade(key_or_token=token)
        self.game = models.Game(**consts.game)
        self.factions = models.Factions.from_dict(data_dict=consts.factions_dict["data"])
        self.notes: str = consts.notes

    async def test_make_new_match(self):
        match = models.NewMatch(game=self.game, weight=self.game.weight, factions=self.factions, notes=self.notes)
        self.assertIsInstance(match, models.NewMatch)
        self.assertIsInstance(match.game, models.Game)
        self.assertIsInstance(match.factions, models.Factions)
        self.assertEqual(match.notes, self.notes)

    async def test_match_as_dict(self):
        match = models.NewMatch(game=self.game, weight=self.game.weight, factions=self.factions, notes=self.notes)
        match_dict = match.as_dict()
        self.assertListEqual(match_dict, consts.match_post_dict["data"])

    async def test_match_as_dict_with_no_game(self):
        match = models.NewMatch(game=self.game, weight=self.game.weight, factions=self.factions, notes=self.notes)
        match.game = None
        match_dict = match.as_dict()
        self.assertListEqual(match_dict, [])

    async def test_add_faction(self):
        players = models.Players.from_dict(data_dict=consts.players_returnvalue["success"])
        rank = 1
        # FYI for some reason points is a string,
        points = "10"
        match = models.NewMatch(game=self.game, weight=self.game.weight, factions=[], notes=self.notes)
        match.add_faction(name="", players=players, rank=rank, points=points)
        self.assertEqual(len(match.factions), 1)
        self.assertIsInstance(match.factions[0], models.Faction)
        self.assertEqual(len(match.factions[0].players), 4)
        self.assertIsInstance(match.factions[0].players, models.Players)
        self.assertIsInstance(match.factions[0].players[0], models.Player)
        self.assertEqual(match.factions[0].rank, rank)
        self.assertEqual(match.factions[0].points, points)

    async def test_add_faction_with_no_players(self):
        rank = 1
        # FYI for some reason points is a string,
        points = "10"
        match = models.NewMatch(game=self.game, weight=self.game.weight, notes=self.notes)
        with self.assertRaises(RankadeException):
            match.add_faction(name="", players=[], rank=rank, points=points)

    async def test_add_faction_with_one_typed_player(self):
        rank = 1
        # FYI for some reason points is a string,
        points = "10"
        player = models.Players.from_dict(data_dict=consts.players_returnvalue["success"])[0]
        self.assertIsInstance(player, models.Player)
        match = models.NewMatch(game=self.game, weight=self.game.weight, notes=self.notes)
        match.add_faction(name="", players=player, rank=rank, points=points)
        self.assertIsInstance(match.factions, models.Factions)
        self.assertEqual(len(match.factions), 1)
        self.assertIsInstance(match.factions[0].players, models.Players)

    async def test_add_bot_faction(self):
        rank = 1
        # for some reason points is a string,
        points = "10"
        match = models.NewMatch(game=self.game, weight=self.game.weight, notes=self.notes)
        match.add_bot_faction(rank=rank, points=points, name="bot")
        self.assertEqual(len(match.factions), 1)
        self.assertIsInstance(match.factions[0], models.Faction)
        self.assertEqual(len(match.factions[0].players), 1)
        self.assertIsInstance(match.factions[0].players, models.Players)
        self.assertIsInstance(match.factions[0].players[0], models.Player)
        self.assertEqual(match.factions[0].rank, rank)
        self.assertEqual(match.factions[0].points, points)
        self.assertTrue(match.factions[0].is_bot)

    async def test_add_bot_faction_with_players(self):
        rank = 1
        # FYI for some reason points is a string,
        points = "10"
        match = models.NewMatch(game=self.game, weight=self.game.weight, factions=[], notes=self.notes)
        with self.assertRaises(RankadeException):
            match.add_faction(
                players=[self.factions[0].players[0], self.factions[1].players[0]],
                rank=rank,
                points=points,
                name="",
                bot=True,
            )


if __name__ == "__main__":
    unittest.main()
