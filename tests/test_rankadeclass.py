import unittest
from unittest.mock import AsyncMock, patch

import rankade
from rankade import models
from rankade.api.Endpoint import Endpoint

from . import consts


class TestRankade(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        token = consts.make_token(consts.valid_token_message)
        self.rankade = rankade.Rankade(key_or_token=token)


class TestRankadeGames(TestRankade):
    @patch(target="rankade.api.Api.Api._request", return_value=consts.games_returnvalue["success"])
    async def test_get_games(self, mock_response: AsyncMock):
        result = await self.rankade.get_games()
        self.assertIsInstance(result, models.Games)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.GAMES)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._request")
    async def test_get_popular_games(self, mock_response: AsyncMock):
        result = self.rankade.get_popular_games()
        with self.assertRaises(NotImplementedError):
            await result
        mock_response.assert_not_called()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.games_returnvalue["success"])
    async def test_game_search(self, mock_response: AsyncMock):
        result = await self.rankade.game_search("twilight")
        self.assertIsInstance(result, models.Games)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.GAMES_SEARCH)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.new_game_returnvalue["success"])
    async def test_new_game_with_bggId(self, mock_response: AsyncMock):
        game_id = 12333
        result = await self.rankade.new_game_with_bggId(game_id)
        self.assertIsInstance(result, models.Game)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.GAME)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()
        self.assertEqual(result.bggIdGame, game_id)

    @patch(target="rankade.api.Api.Api._request", return_value=consts.new_game_returnvalue["success"])
    async def test_new_game_with_name(self, mock_response: AsyncMock):
        game_name = "Twilight Struggle"
        result = await self.rankade.new_game_with_name(game_name)
        self.assertIsInstance(result, models.Game)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.GAME)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()
        self.assertEqual(result.name, game_name)


class TestRankadeMatch(TestRankade):
    @patch(target="rankade.api.Api.Api._request", return_value=consts.matches_status_returnvalue["success"])
    async def test_get_match_status(self, mock_response: AsyncMock):
        result = await self.rankade.get_match_status()
        self.assertIsInstance(result, models.MatchStatus)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.MATCH_STATUS)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.matches_returnvalue_page_2["success"])
    async def test_get_all_matches(self, mock_response: AsyncMock):
        result = await self.rankade.get_all_matches()
        self.assertIsInstance(result, models.Matches)
        self.assertEqual(len(result), 3)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.MATCHES)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.matches_returnvalue_page_2["success"])
    async def test_get_match_with_id(self, mock_response: AsyncMock):
        match_id = "Jowlqr5o0qA"
        result = await self.rankade.get_match_with_id(match_id)
        self.assertIsInstance(result, models.Match)
        self.assertEqual(result.id, match_id)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.MATCHES)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.matches_returnvalue_page_2["success"])
    async def test_get_matches_with_players_with_valid_id(self, mock_response: AsyncMock):
        player_ids = ["JVk1OklO1ov"]
        result = await self.rankade.get_matches_with_players(player_ids=player_ids)
        self.assertIsInstance(result, models.Matches)
        self.assertIsInstance(result[0], models.Match)
        self.assertIn(player_ids[0], result[0].player_ids)
        mock_response.assert_called()
        mock_response.assert_awaited()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.matches_returnvalue_page_2["success"])
    async def test_get_matches_with_players_with_invalid_id(self, mock_response: AsyncMock):
        player_ids = ["INVALIDID"]
        result = await self.rankade.get_matches_with_players(player_ids=player_ids)
        self.assertIsInstance(result, models.Matches)
        self.assertEqual(len(result), 0)
        mock_response.assert_called()
        mock_response.assert_awaited()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.matches_returnvalue_page_2["success"])
    async def test_get_match_number(self, mock_response: AsyncMock):
        match_number = 3
        result = await self.rankade.get_match_number(match_number)
        self.assertIsInstance(result, models.Match)
        self.assertEqual(result.number, match_number)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.MATCHES)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()


class TestRankadeMatchSave(TestRankade):
    @classmethod
    def setUpClass(cls):
        game = models.Game(**consts.game)
        factions = models.Factions.from_dict(data_dict=consts.factions_dict["data"])
        cls.match = models.NewMatch(game=game, notes=consts.notes, factions=factions)

    @patch(target="rankade.api.Api.Api._request", return_value=consts.match_post_returnvalue["success"])
    async def test_match_save(self, mock_response: AsyncMock):
        _ = await self.rankade.save_match(match=TestRankadeMatchSave.match)
        call = mock_response.call_args[0][0]
        self.assertIs(call.endpoint, Endpoint.MATCH)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()
        self.assertListEqual(call.json, consts.match_post_dict["data"])

    @patch(target="rankade.api.Api.Api._request", return_value=consts.match_post_returnvalue["success"])
    async def test_match_save_with_dryrun(self, mock_response: AsyncMock):
        _ = await self.rankade.save_match(match=TestRankadeMatchSave.match, dry_run=True)
        call = mock_response.call_args[0][0]
        self.assertIs(call.endpoint, Endpoint.MATCH)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()
        self.assertListEqual(call.json, consts.match_post_dict["data"])
        self.assertTrue(call.params["dryrun"])


class TestRankadePlayers(TestRankade):
    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.players_returnvalue["success"])
    async def test_get_all_players(self, mock_response: AsyncMock):
        result = await self.rankade.get_all_players()
        self.assertIsInstance(result, models.Players)
        self.assertEqual(len(result), 4)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.PLAYERS)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.new_ghost_player_returnvalue["success"])
    async def test_new_ghost_player(self, mock_response: AsyncMock):
        player_name = "Emmephisto"
        result = await self.rankade.new_ghost_player(player_name)
        self.assertIsInstance(result, models.Player)
        self.assertEqual(result.displayName, f"*{player_name}")
        self.assertTrue(result.is_ghost)
        self.assertFalse(result.username)

    @patch(target="rankade.api.Api.Api._request", return_value=consts.match_post_returnvalue["success"])
    async def test_save_match(self, mock_response: AsyncMock):
        game = models.Game(**consts.game)
        factions = models.Factions.from_dict(data_dict=consts.factions_dict)
        match = models.NewMatch(game=game, factions=factions, notes=consts.notes)
        await self.rankade.save_match(match=match)
        call = mock_response.call_args[0][0]
        self.assertEqual(call.endpoint, Endpoint.MATCH)
        self.assertListEqual(call.json, consts.match_post_dict["data"])


class TestRankadeQuota(TestRankade):
    @patch(target="rankade.api.Api.Api._request", return_value=consts.quota_returnvalue["success"])
    async def test_get_quota(self, mock_response: AsyncMock):
        result = await self.rankade.get_quota()
        self.assertIsInstance(result, models.Quota)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.QUOTA)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()


class TestRankadeRankings(TestRankade):
    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.rankings_returnvalue["success"])
    async def test_get_rankings(self, mock_response: AsyncMock):
        result = await self.rankade.get_rankings()
        self.assertIsInstance(result, models.Rankings)
        self.assertIsInstance(result[0], models.Ranking)
        self.assertEqual(len(result), 4)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.RANKINGS)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.rankings_returnvalue["success"])
    async def test_get_rankings_with_subset_id(self, mock_response: AsyncMock):
        subset_id = "oBypZD7Vngx"
        result = await self.rankade.get_rankings(subset_id=subset_id)
        called_with = mock_response.call_args_list[0][0][0]
        self.assertIsInstance(result, models.Rankings)
        self.assertIsInstance(result[0], models.Ranking)
        self.assertEqual(len(result), 4)
        self.assertEqual(called_with.path, f"rankings/{subset_id}/last/1")
        self.assertEqual(called_with.subset, subset_id)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.RANKINGS)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.rankings_returnvalue["success"])
    async def test_get_rankings_with_match_number(self, mock_response: AsyncMock):
        match_number = 3
        result = await self.rankade.get_rankings(match_number=match_number)
        called_with = mock_response.call_args_list[0][0][0]
        self.assertIsInstance(result, models.Rankings)
        self.assertIsInstance(result[0], models.Ranking)
        self.assertEqual(called_with.path, f"rankings/{match_number}/1")
        self.assertEqual(called_with.match, match_number)
        self.assertEqual(len(result), 4)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.RANKINGS)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._paginated_request", return_value=consts.rankings_returnvalue["success"])
    async def test_get_rankings_with_match_number_and_subset_id(self, mock_response: AsyncMock):
        match_number = 3
        subset_id = "oBypZD7Vngx"
        result = await self.rankade.get_rankings(subset_id=subset_id, match_number=match_number)
        called_with = mock_response.call_args_list[0][0][0]

        self.assertIsInstance(result, models.Rankings)
        self.assertIsInstance(result[0], models.Ranking)
        self.assertEqual(called_with.path, f"rankings/{subset_id}/{match_number}/1")
        self.assertEqual(called_with.match, match_number)
        self.assertEqual(called_with.subset, subset_id)
        self.assertEqual(len(result), 4)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.RANKINGS)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()


class TestRankadeSubsets(TestRankade):
    @patch(target="rankade.api.Api.Api._request", return_value=consts.subsets_returnvalue["success"])
    async def test_get_subset_with_id(self, mock_response: AsyncMock):
        subset_id = "oBypZD7Vngx"
        result = await self.rankade.get_subset_with_id(id=subset_id)
        self.assertIsInstance(result, models.Subset)
        self.assertEqual(result.id, subset_id)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.SUBSET)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()

    @patch(target="rankade.api.Api.Api._request", return_value=consts.subsets_returnvalue["success"])
    async def test_get_subsets(self, mock_response: AsyncMock):
        result = await self.rankade.get_subsets()
        self.assertIsInstance(result, models.Subsets)
        self.assertIsInstance(result[0], models.Subset)
        self.assertEqual(len(result), 3)
        call = mock_response.call_args[0][0].endpoint
        self.assertIs(call, Endpoint.SUBSET)
        mock_response.assert_called_once()
        mock_response.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
