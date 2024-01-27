import json
import unittest
from datetime import datetime
from typing import Dict, List

from rankade import models
from rankade.api import RankadeResponse
from rankade.api.Token import Token

from . import consts


class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_token = consts.make_token(consts.valid_token_message)
        cls.invalid_token = consts.make_token(consts.invalid_token_message)

    ## Check matches
    def check_match_Jowlqr5o0qA(self, match: models.Match) -> None:
        self.assertIsInstance(match, models.Match)
        self.assertEqual(match.id, "Jowlqr5o0qA")
        self.assertEqual(match.externalId, "")
        self.assertIsInstance(match.date, datetime)
        self.assertEqual(match.date, datetime.fromisoformat("2019-12-20 10:45:00"))
        self.assertIsInstance(match.registrationDate, datetime)
        self.assertEqual(match.registrationDate, datetime.fromisoformat("2019-12-20 10:46:01"))
        self.assertEqual(match.number, 3)
        self.assertEqual(match.summary, "Captain Nemo\nLongJohn")
        self.assertEqual(match.type, "player_vs_player")
        self.assertEqual(match.draw, 0)
        self.assertEqual(match.weight, "normal")
        self.assertEqual(match.weightLabel, "Normal")
        self.assertEqual(match.notes, "")
        self.assertIsInstance(match.game, models.Game)
        self.check_game_table_tennis_1334(match.game)

        self.assertIsInstance(match.factions[0], models.Faction)

        self.assertEqual(match.factions[0].rank, 1)
        self.assertEqual(match.factions[0].name, "")
        self.assertEqual(match.factions[0].points, 21)
        self.assertEqual(match.factions[0].countPlayers, 1)
        self.assertEqual(match.factions[0].winner, 1)
        self.assertEqual(match.factions[0].bot, 0)
        self.check_player_captain_nemo(match.factions[0].players[0])
        self.assertEqual(match.factions[1].rank, 2)
        self.assertEqual(match.factions[1].name, "")
        self.assertEqual(match.factions[1].points, 16)
        self.assertEqual(match.factions[1].countPlayers, 1)
        self.assertEqual(match.factions[1].winner, 0)
        self.assertEqual(match.factions[1].bot, 0)
        self.check_player_longjohn(match.factions[1].players[0])

        self.assertIsInstance(match.factions[0].players, models.Players)
        self.assertIsInstance(match.factions[0].players[0], models.Player)
        self.assertIsInstance(match.factions[1].players[0], models.Player)

    def check_match_kMAxQ8GRYOq(self, match: models.Match) -> None:
        self.assertIsInstance(match, models.Match)
        self.assertEqual(match.id, "kMAxQ8GRYOq")
        self.assertEqual(match.externalId, "")
        self.assertIsInstance(match.date, datetime)
        self.assertEqual(match.date, datetime.fromisoformat("2019-12-20 10:19:34"))
        self.assertIsInstance(match.registrationDate, datetime)
        self.assertEqual(match.registrationDate, datetime.fromisoformat("2019-12-20 10:20:12"))
        self.assertEqual(match.number, 2)
        self.assertEqual(match.summary, "MackmanSoup\nLongJohn")
        self.assertEqual(match.type, "player_vs_player")
        self.assertEqual(match.draw, 0)
        self.assertEqual(match.weight, "normal")
        self.assertEqual(match.weightLabel, "Normal")
        self.assertEqual(match.notes, "Weather was fine")
        self.assertIsInstance(match.game, models.Game)
        self.check_game_table_tennis_1334(match.game)

        self.assertIsInstance(match.factions[0], models.Faction)

        self.assertEqual(match.factions[0].rank, 1)
        self.assertEqual(match.factions[0].name, "")
        self.assertEqual(match.factions[0].points, 21)
        self.assertEqual(match.factions[0].countPlayers, 1)
        self.assertEqual(match.factions[0].winner, 1)
        self.assertEqual(match.factions[0].bot, 0)
        self.check_player_mackmansoup(match.factions[0].players[0])
        self.assertEqual(match.factions[1].rank, 2)
        self.assertEqual(match.factions[1].name, "")
        self.assertEqual(match.factions[1].points, 9)
        self.assertEqual(match.factions[1].countPlayers, 1)
        self.assertEqual(match.factions[1].winner, 0)
        self.assertEqual(match.factions[1].bot, 0)
        self.check_player_longjohn(match.factions[1].players[0])

        self.assertIsInstance(match.factions[0].players, models.Players)
        self.assertIsInstance(match.factions[0].players[0], models.Player)
        self.assertIsInstance(match.factions[1].players[0], models.Player)

    def check_match_kRplW5enYqE(self, match: models.Match) -> None:
        self.assertEqual(match.id, "kRplW5enYqE")
        self.assertEqual(match.externalId, "")
        self.assertIsInstance(match.date, datetime)
        self.assertEqual(match.date, datetime.fromisoformat("2019-12-20 09:25:28"))
        self.assertIsInstance(match.registrationDate, datetime)
        self.assertEqual(match.registrationDate, datetime.fromisoformat("2019-12-20 09:25:48"))
        self.assertEqual(match.number, 1)
        self.assertEqual(match.summary, "LongJohn\nCaptain Nemo")
        self.assertEqual(match.type, "player_vs_player")
        self.assertEqual(match.draw, 0)
        self.assertEqual(match.weight, "normal")
        self.assertEqual(match.weightLabel, "Normal")
        self.assertEqual(match.notes, "")
        self.check_game_table_tennis_1334(match.game)

        self.assertEqual(match.factions[0].rank, 1)
        self.assertEqual(match.factions[0].name, "")
        self.assertEqual(match.factions[0].points, 21)
        self.assertEqual(match.factions[0].countPlayers, 1)
        self.assertEqual(match.factions[0].winner, 1)
        self.assertEqual(match.factions[0].bot, 0)
        self.check_player_longjohn(match.factions[0].players[0])
        self.assertEqual(match.factions[1].rank, 2)
        self.assertEqual(match.factions[1].name, "")
        self.assertEqual(match.factions[1].points, 18)
        self.assertEqual(match.factions[1].countPlayers, 1)
        self.assertEqual(match.factions[1].winner, 0)
        self.assertEqual(match.factions[1].bot, 0)
        self.check_player_captain_nemo(match.factions[1].players[0])

        self.assertIsInstance(match.factions[0].players, models.Players)
        self.assertIsInstance(match.factions[0].players[0], models.Player)
        self.assertIsInstance(match.factions[1].players[0], models.Player)
        self.assertDictEqual(match.factions[0].as_dict(), consts.faction_dict)
        self.assertTrue(match.factions[0].is_winner)

    def check_match_kRplW5vnYqE(self, match: models.Match) -> None:
        self.assertEqual(match.id, "kRplW5vnYqE")
        self.assertEqual(match.externalId, "")
        self.assertIsInstance(match.date, datetime)
        self.assertEqual(match.date, datetime.fromisoformat("2019-12-20 09:34:54"))
        self.assertIsInstance(match.registrationDate, datetime)
        self.assertEqual(match.registrationDate, datetime.fromisoformat("2019-12-20 09:35:32"))
        self.assertEqual(match.number, 1)
        self.assertEqual(match.summary, "Emmephisto\nMackmanSoup")
        self.assertEqual(match.type, "player_vs_player")
        self.assertEqual(match.draw, 0)
        self.assertEqual(match.weight, "normal")
        self.assertEqual(match.weightLabel, "Normal")
        self.assertEqual(match.notes, "")
        self.check_game_table_tennis_1334(match.game)
        self.assertEqual(match.factions[0].rank, 1)
        self.assertEqual(match.factions[0].name, "")
        self.assertEqual(match.factions[0].points, 21)
        self.assertEqual(match.factions[0].countPlayers, 1)
        self.assertEqual(match.factions[0].winner, 1)
        self.assertEqual(match.factions[0].bot, 0)
        self.check_player_emmephisto(match.factions[0].players[0])
        self.assertEqual(match.factions[1].rank, 2)
        self.assertEqual(match.factions[1].name, "")
        self.assertEqual(match.factions[1].points, 19)
        self.assertEqual(match.factions[1].countPlayers, 1)
        self.assertEqual(match.factions[1].winner, 0)
        self.assertEqual(match.factions[1].bot, 0)
        self.check_player_mackmansoup(match.factions[1].players[0])

        self.assertIsInstance(match.factions[0].players, models.Players)
        self.assertIsInstance(match.factions[0].players[0], models.Player)
        self.assertIsInstance(match.factions[1].players[0], models.Player)

        self.assertFalse(match.is_draw)
        self.assertListEqual(match.winning_factions, [match.factions[0]])
        self.assertListEqual(match.winning_players, [match.factions[0].players[0]])

    ## Check games
    def check_game_twilight_imperium_962(self, game: models.Game) -> None:
        self.assertIsInstance(game, models.Game)
        self.assertEqual(game.id, 962)
        self.assertEqual(game.name, "Twilight Imperium (Third Edition)")
        self.assertEqual(game.weight, "normal")
        self.assertEqual(game.weightLabel, "Normal")
        self.assertEqual(
            game.thumbnail,
            "https://cf.geekdo-images.com/thumb/img/fED6XRJVDYYOppNNmRfuU1vJr8Q=/fit-in/200x150/pic4128153.jpg",
        )
        self.assertEqual(
            game.mediumImage, "https://userscontents.rankade.com/images/500/4bdae1da8be6ecb837d0f8567ddb100e.jpg"
        )
        self.assertEqual(game.bggIdGame, 12493)

    def check_game_twilight_imperium_4579(self, game: models.Game) -> None:
        self.assertIsInstance(game, models.Game)
        self.assertEqual(game.id, 4579)
        self.assertEqual(game.name, "Twilight Imperium: Fourth Edition")
        self.assertEqual(game.weight, "normal")
        self.assertEqual(game.weightLabel, "Normal")
        self.assertEqual(
            game.thumbnail,
            "https://cf.geekdo-images.com/thumb/img/UOV5jJadzHc6ebYd5CfZXGbOWsc=/fit-in/200x150/pic3727516.jpg",
        )
        self.assertEqual(
            game.mediumImage,
            "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/956d6ab81f37aef3db55d5909cf92ab8.jpg",
        )
        self.assertEqual(game.bggIdGame, 233078)

    def check_game_twilight_squabble_4784(self, game: models.Game) -> None:
        self.assertIsInstance(game, models.Game)
        self.assertEqual(game.id, 4784)
        self.assertEqual(game.name, "Twilight Squabble")
        self.assertEqual(game.weight, "normal")
        self.assertEqual(game.weightLabel, "Normal")
        self.assertEqual(
            game.thumbnail,
            "https://cf.geekdo-images.com/thumb/img/BOsJzM6uF6GdjaGd8i45xvQ_16U=/fit-in/200x150/pic2908587.png",
        )
        self.assertEqual(
            game.mediumImage,
            "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/3f00c90fea5f03698038df48c584e799.png",
        )
        self.assertEqual(game.bggIdGame, 191364)

    def check_game_twilight_struggle_963(self, game: models.Game) -> None:
        self.assertIsInstance(game, models.Game)
        self.assertEqual(game.id, 963)
        self.assertEqual(game.name, "Twilight Struggle")
        self.assertEqual(game.weight, "normal")
        self.assertEqual(game.weightLabel, "Normal")
        self.assertEqual(
            game.thumbnail,
            "https://cf.geekdo-images.com/thumb/img/mEmeJrI3AbGTpWyeFOZnR0s_LcY=/fit-in/200x150/pic361592.jpg",
        )
        self.assertEqual(
            game.mediumImage,
            "https://userscontents.rankade.com/images/500/6f2f6d3c4ec73f443527a808a62b0261.jpg",
        )
        self.assertEqual(game.bggIdGame, 12333)

    def check_game_table_tennis_1334(self, game: models.Game) -> None:
        self.assertEqual(game.id, 1334)
        self.assertEqual(game.name, "Table Tennis")
        self.assertEqual(game.weight, "normal")
        self.assertEqual(game.weightLabel, "Normal")
        self.assertEqual(
            game.thumbnail,
            "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/table_tennis.jpg",
        )
        self.assertEqual(
            game.mediumImage,
            "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/500/table_tennis.jpg",
        )
        self.assertIsNone(game.bggIdGame)

    ## Check subsets
    def check_subset_oBypZD7Vngx(self, subset: models.Subset) -> None:
        self.assertIsInstance(subset, models.Subset)
        self.assertEqual(subset.id, "oBypZD7Vngx")
        self.assertEqual(subset.name, "Main")
        self.assertEqual(subset.type, "main")
        self.assertIsInstance(subset.creationDate, datetime)
        self.assertEqual(subset.creationDate, datetime.fromisoformat("2019-12-20 09:23:48"))
        self.assertEqual(subset.isMain, 1)
        self.assertEqual(subset.isCustom, 0)
        self.assertEqual(subset.icon, "https://userscontents.rankade.com/images/256/game_icon_placeholder.png")
        self.assertIsNone(subset.game)
        self.assertEqual(subset.countMatches, 47)
        self.assertIsInstance(subset.firstMatch, models.Match)
        self.check_match_kRplW5enYqE(subset.firstMatch)
        self.check_match_Jowlqr5o0qA(subset.lastMatch)
        self.assertIsInstance(subset.firstMatch.game, models.Game)

        self.check_game_table_tennis_1334(subset.firstMatch.game)
        self.assertIsInstance(subset.firstMatch.factions[0], models.Faction)
        self.assertEqual(subset.firstMatch.factions[0].rank, 1)
        self.assertEqual(subset.firstMatch.factions[0].name, "")
        self.assertEqual(subset.firstMatch.factions[0].points, 21)
        self.assertEqual(subset.firstMatch.factions[0].countPlayers, 1)
        self.assertEqual(subset.firstMatch.factions[0].winner, 1)
        self.assertEqual(subset.firstMatch.factions[0].bot, 0)
        self.assertFalse(subset.firstMatch.factions[0].is_bot)

        self.assertIsInstance(subset.firstMatch.factions[0].players, models.Players)
        self.assertIsInstance(subset.firstMatch.factions[0].players[0], models.Player)
        self.check_player_longjohn(subset.firstMatch.factions[0].players[0])
        self.check_player_captain_nemo(subset.firstMatch.factions[1].players[0])

        self.assertEqual(subset.matches[0], subset.firstMatch)
        self.assertEqual(subset.matches[1], subset.lastMatch)

    ## Check Players
    def check_player_longjohn(self, player: models.Player) -> None:
        self.assertEqual(player.id, "Dwog3w8mgAL")
        self.assertEqual(player.ghost, 1)
        self.assertEqual(player.username, "")
        self.assertEqual(player.displayName, "*LongJohn")
        self.assertEqual(player.icon, "")
        self.assertTrue(player.is_ghost)

    def check_player_captain_nemo(self, player: models.Player) -> None:
        self.assertEqual(player.id, "JVk1OklO1ov")
        self.assertEqual(player.ghost, 1)
        self.assertEqual(player.username, "")
        self.assertEqual(player.displayName, "*Captain Nemo")
        self.assertEqual(player.icon, "")
        self.assertTrue(player.is_ghost)

    def check_player_mackmansoup(self, player: models.Player) -> None:
        self.assertEqual(player.id, "37VjKRy1a6p")
        self.assertEqual(player.ghost, 0)
        self.assertEqual(player.username, "Mackmansoup4585")
        self.assertEqual(player.displayName, "Mackmansoup")
        self.assertEqual(
            player.icon,
            "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png",
        )
        self.assertFalse(player.is_ghost)

    def check_player_emmephisto(self, player: models.Player) -> None:
        self.assertEqual(player.id, "zqRjGDw4gbJ")
        self.assertEqual(player.ghost, 1)
        self.assertEqual(player.username, "")
        self.assertEqual(player.displayName, "*Emmephisto")
        self.assertEqual(player.icon, "")
        self.assertTrue(player.is_ghost)


class TestToken(TestModels):
    def test_token_from_dict_bad_token(self) -> None:
        token_response = RankadeResponse(**consts.token_returnvalue).success
        with self.assertLogs(level="CRITICAL"):
            token = Token(**token_response)
            self.assertEqual(token.token, "jwt-token-here")
            self.assertEqual(token.bearer, "Bearer jwt-token-here")
            self.assertTrue(token.is_invalid)

    def test_expired_token(self) -> None:
        token = Token(token=TestToken.invalid_token)
        self.assertEqual(token.token, TestToken.invalid_token)
        self.assertEqual(token.bearer, f"Bearer {TestToken.invalid_token}")
        self.assertTrue(token.is_invalid)

    def test_valid_token(self) -> None:
        token = Token(token=TestToken.valid_token)
        self.assertEqual(token.token, TestToken.valid_token)
        self.assertEqual(token.bearer, f"Bearer {TestToken.valid_token}")
        self.assertFalse(token.is_invalid)


class TestErrors(TestModels):
    def test_single_error_from_dict(self) -> None:
        errors_response = RankadeResponse(**consts.errors_returnvalue)
        errors = models.Errors.from_dict(
            data_dict=errors_response.errors,
        )
        errors.url = "http://www.abc.com"
        errors.verb = "Get"
        errors.status = 200

        self.assertIsInstance(errors, models.Errors)
        self.assertIsInstance(errors[0], models.Error)
        self.assertEqual(errors[0].code, "A002")
        self.assertEqual(errors[0].message, "Authentication required")
        self.assertEqual(errors.url, "http://www.abc.com")
        self.assertEqual(errors.verb, "Get")
        self.assertEqual(errors.status, 200)

    def test_multiple_errors_from_dict(self) -> None:
        errors_multi_response = RankadeResponse(**consts.errors_multi_returnvalue)
        errors_multi = models.Errors.from_dict(data_dict=errors_multi_response.errors)
        errors_multi.url = "http://www.abc.com"
        errors_multi.verb = "Get"
        errors_multi.status = 403

        self.assertIsInstance(errors_multi, models.Errors)
        self.assertIsInstance(errors_multi[0], models.Error)
        self.assertIsInstance(errors_multi[1], models.Error)
        self.assertEqual(len(errors_multi), 2)
        self.assertEqual(errors_multi[0].code, "A002")
        self.assertEqual(errors_multi[0].message, "Authentication required")

        self.assertEqual(errors_multi[1].code, "A003")
        self.assertEqual(errors_multi[1].message, "Authentication required #2")
        self.assertEqual(errors_multi.url, "http://www.abc.com")
        self.assertEqual(errors_multi.verb, "Get")
        self.assertEqual(errors_multi.status, 403)


class TestGames(TestModels):
    def test_games_from_dict(self) -> None:
        games_response = RankadeResponse(**consts.games_returnvalue).success
        games = models.Games.from_dict(data_dict=games_response)
        self.assertIsInstance(games, models.Games)
        self.assertEqual(len(games), 4)
        self.check_game_twilight_imperium_962(game=games[0])
        self.check_game_twilight_imperium_4579(game=games[1])
        self.check_game_twilight_squabble_4784(game=games[2])
        self.check_game_twilight_struggle_963(game=games[3])


class TestMatches(TestModels):
    def test_matches_from_dict(self) -> None:
        mathes_str = json.dumps(consts.matches_returnvalue_page_2)
        matches_response = RankadeResponse(**json.loads(mathes_str)).success
        matches = models.Matches.from_dict(data_dict=matches_response)
        self.assertIsInstance(matches, models.Matches)
        self.assertEqual(matches.page, 2)
        self.assertEqual(matches.totalPages, 2)
        self.assertEqual(matches.rowsForPage, 25)
        self.assertEqual(matches.totalMatches, 28)
        self.check_match_Jowlqr5o0qA(match=matches[0])
        self.check_match_kMAxQ8GRYOq(match=matches[1])
        self.check_match_kRplW5vnYqE(match=matches[2])
        self.assertIsInstance(matches.all_players(), models.Players)
        self.assertIsInstance(matches.all_players()[0], models.Player)
        self.assertEqual(len(matches.all_players()), 4)

    def test_matches_post_response_from_dict(self) -> None:
        match_post_response = RankadeResponse(**consts.match_post_returnvalue).success
        match_post = models.NewMatchResponse(**match_post_response)
        self.assertIsInstance(match_post, models.NewMatchResponse)
        self.assertIsInstance(match_post.accepted, models.NewMatchReturnList)
        self.assertIsInstance(match_post.rejected, models.NewMatchReturnList)
        self.assertEqual(match_post.total, 2)
        self.assertEqual(match_post.acceptedCount, 1)
        self.assertEqual(match_post.rejectedCount, 1)

        self.assertIsInstance(match_post.accepted[0], models.NewMatchReturn)
        self.assertIsInstance(match_post.rejected[0], models.NewMatchReturn)
        self.assertEqual(match_post.accepted[0].index, 0)
        self.assertEqual(match_post.accepted[0].id, "wweq")
        self.assertIsNone(match_post.accepted[0].name)
        self.assertEqual(len(match_post.accepted[0].errors), 0)

        self.assertEqual(match_post.rejected[0].index, 1)
        self.assertEqual(match_post.rejected[0].id, "312")
        self.assertIsNone(match_post.rejected[0].name)
        self.assertEqual(len(match_post.rejected[0].errors), 1)
        self.assertIsInstance(match_post.rejected[0].errors, models.Errors)
        self.assertIsInstance(match_post.rejected[0].errors[0], models.Error)
        self.assertEqual(match_post.rejected[0].errors[0].code, "M003")
        self.assertEqual(
            match_post.rejected[0].errors[0].message, "A match with the same external identifier was already accepted"
        )
        self.assertTrue(match_post.has_error)

    def test_matches_status_from_dict(self) -> None:
        matches_status_response = RankadeResponse(**consts.matches_status_returnvalue).success
        matches_status = models.MatchStatus(**matches_status_response)
        self.assertEqual(matches_status.queued, 0)
        self.assertEqual(matches_status.waiting, 0)
        self.assertEqual(matches_status.added, 83)
        self.assertEqual(matches_status.processed, 83)
        self.assertEqual(matches_status.total, 83)


class TestPlayers(TestModels):
    def test_players_from_dict(self) -> None:
        players_response = RankadeResponse(**consts.players_returnvalue).success
        players = models.Players.from_dict(data_dict=players_response)
        self.assertIsInstance(players, models.Players)
        self.assertEqual(players.page, 1)
        self.assertEqual(players.totalPages, 1)
        self.assertEqual(players.rowsForPage, 25)
        self.assertEqual(players.totalPlayers, len(players))

        # Check player objects
        self.assertEqual(len(players), 4)
        self.assertIsInstance(players[0], models.Player)
        self.assertIsInstance(players[1], models.Player)
        self.assertIsInstance(players[2], models.Player)
        self.assertIsInstance(players[3], models.Player)
        self.check_player_mackmansoup(player=players[0])
        self.check_player_emmephisto(player=players[1])
        self.check_player_longjohn(player=players[2])
        self.check_player_captain_nemo(player=players[3])
        # Check players object properties
        self.assertIsInstance(players.ids, List)
        self.assertEqual(len(players.ids), 4)
        self.assertListEqual(players.ids, ["37VjKRy1a6p", "zqRjGDw4gbJ", "Dwog3w8mgAL", "JVk1OklO1ov"])

        self.assertIsInstance(players.ghosts, List)
        self.assertEqual(len(players.ghosts), 3)
        self.assertIsInstance(players.ghosts[0], models.Player)
        self.assertIsInstance(players.ghosts[1], models.Player)
        self.assertIsInstance(players.ghosts[2], models.Player)
        self.check_player_emmephisto(players.ghosts[0])
        self.check_player_longjohn(players.ghosts[1])
        self.check_player_captain_nemo(players.ghosts[2])

        self.assertIsInstance(players.display_names, List)
        self.assertEqual(len(players.display_names), 4)
        self.assertListEqual(players.display_names, ["Mackmansoup", "*Emmephisto", "*LongJohn", "*Captain Nemo"])
        self.assertIsInstance(players.display_names_clean, List)
        self.assertEqual(len(players.display_names_clean), 4)
        self.assertListEqual(players.display_names_clean, ["Mackmansoup", "Emmephisto", "LongJohn", "Captain Nemo"])
        self.assertIsInstance(players.usernames, List)
        self.assertEqual(len(players.usernames), 1)
        self.assertIsInstance(players.usernames[0], str)
        self.assertListEqual(players.usernames, ["Mackmansoup4585"])
        self.assertIsInstance(players.icons, Dict)
        icons_dict = {
            "37VjKRy1a6p": "https://rnkdusrsctnts-mlseauq9snbpoibmw.netdna-ssl.com/images/256/16e4fd77ad4ead03683febd462ffe023.png"
        }
        self.assertDictEqual(players.icons, icons_dict)


class TestQuotas(TestModels):
    def test_quotas_from_dict(self) -> None:
        quota_response = RankadeResponse(**consts.quota_returnvalue).success
        quota = models.Quota(**quota_response)
        self.assertEqual(quota.callsPerYear, "2%")
        self.assertEqual(quota.callsPerHour, "12%")
        self.assertEqual(quota.matchesPerYear, "3%")
        self.assertEqual(quota.matchesPerDay, "15%")
        self.assertEqual(quota.matchesPerHour, "0%")
        self.assertEqual(quota.rankingCallsPerYear, "2%")
        self.assertEqual(quota.rankingCallsPerDay, "5%")
        self.assertEqual(quota.rankingCallsPerHour, "10%")
        self.assertEqual(quota.apiCreatedGames, "1%")


class TestRankings(TestModels):
    def test_rankings_from_dict(self) -> None:
        rankings_str = json.dumps(consts.rankings_returnvalue)
        rankings_response = RankadeResponse(**json.loads(rankings_str)).success
        rankings = models.Rankings.from_dict(data_dict=rankings_response)
        # rankings type testing
        self.assertIsInstance(rankings, models.Rankings)
        self.assertEqual(len(rankings), 4)
        self.assertIsInstance(rankings[0], models.Ranking)
        self.assertIsInstance(rankings[0].player, models.Player)
        # ranking value testing
        self.assertEqual(rankings.page, 1)
        self.assertEqual(rankings.totalPages, 1)
        self.assertEqual(rankings.rowsForPage, 25)
        self.assertEqual(rankings[0].ree, 2043)
        self.assertEqual(rankings[0].deltaRee, -2)
        self.assertEqual(rankings[0].position, 26)
        self.assertEqual(rankings[0].deltaPosition, 0)
        self.assertEqual(rankings[0].belt, 0)
        self.assertEqual(rankings[0].beltLabel, "")
        self.assertEqual(rankings[0].title, 4)
        self.assertEqual(rankings[0].titleLabel, "")
        self.assertEqual(rankings[0].status, 3)
        self.assertEqual(rankings[0].statusLabel, "active")
        # ranking player value testing
        self.check_player_emmephisto(rankings[0].player)
        self.check_player_mackmansoup(rankings[1].player)
        self.check_player_captain_nemo(rankings[2].player)
        self.check_player_longjohn(rankings[3].player)

        # subset testing
        self.assertIsInstance(rankings.subset, models.Subset)
        self.check_subset_oBypZD7Vngx(rankings.subset)

        # match testing
        self.assertIsInstance(rankings.match, models.Match)
        self.check_match_Jowlqr5o0qA(rankings.match)
        self.assertListEqual(rankings.sorted_by_position, [rankings[0], rankings[1], rankings[2], rankings[3]])
        self.check_player_emmephisto(rankings.sorted_by_position[0].player)
        self.assertListEqual(rankings.sorted_by_delta_position, [rankings[2], rankings[1], rankings[0], rankings[3]])
        self.check_player_captain_nemo(rankings.sorted_by_delta_position[0].player)
        self.assertListEqual(rankings.sorted_by_ree, [rankings[0], rankings[1], rankings[2], rankings[3]])
        self.check_player_emmephisto(rankings.sorted_by_ree[0].player)
        self.assertListEqual(rankings.sorted_by_delta_ree, [rankings[2], rankings[1], rankings[0], rankings[3]])
        self.check_player_captain_nemo(rankings.sorted_by_delta_ree[0].player)


class TestSubsets(TestModels):
    def test_subsets_from_dict(self) -> None:
        subsets_str = json.dumps(consts.subsets_returnvalue)
        subsets_response = RankadeResponse(**json.loads(subsets_str)).success
        subsets = models.Subsets.from_dict(data_dict=subsets_response)
        self.assertIsInstance(subsets, models.Subsets)
        self.check_subset_oBypZD7Vngx(subsets[0])


if __name__ == "__main__":
    unittest.main()
