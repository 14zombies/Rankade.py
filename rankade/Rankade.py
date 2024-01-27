# rankade.Rankade.py
from typing import MutableSequence, Optional, Union

import aiohttp

import rankade.models as models
from rankade.api import Api, Endpoint
from rankade.api.Api import PARAMS


class Rankade(object):
    """Main wrapper around the Rankade Api. Use this class along with it's methods to access the Api."""

    def __init__(
        self,
        key_or_token: str,
        secret: Optional[str] = None,
        base_url: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ):
        self._api = Api(key_or_token, secret, base_url=base_url, session=session)

    """
    Games
    """

    async def get_games(self) -> models.Games:
        """Returns the list of the group's games (i.e. games with at least one match played within the group)."""
        async with self._api as api:
            games_response = await api.request(endpoint=Endpoint.GAMES)
            return models.Games.from_dict(data_dict=games_response)

    async def get_popular_games(self) -> models.Games:
        """
        Not implemented on server, is in API documentation, but requests return an error.

        :raises: NotImplementedError
        """
        raise NotImplementedError("Not implimented on server, request returns an error.")

        # If ever gets implimented on server this should be uncommented.
        # async with self._api as api:
        #   games_attributes = await self._api.request(endpoint=Endpoint.POPULAR)
        #   return models.Games.from_dict(data_dict=games_attributes)

    async def game_search(self, name: str) -> models.Games:
        """
        Searches games by name.

        :param name: Name of game to be searched for
        """
        async with self._api as api:
            search_endpoint = Endpoint.GAMES_SEARCH
            params: PARAMS = {"name": name}
            games_response = await api.request(endpoint=search_endpoint, params=params)
            return models.Games.from_dict(data_dict=games_response)

    async def new_game_with_bggId(self, bggId: int) -> models.Game:
        params: PARAMS = {"bggId": bggId}
        return await self._new_game_with(params=params)

    async def new_game_with_name(self, name: str) -> models.Game:
        params: PARAMS = {"name": name}
        return await self._new_game_with(params=params)

    async def _new_game_with(self, params: PARAMS) -> models.Game:
        async with self._api as api:
            result = await api.request(endpoint=Endpoint.GAME, params=params)
            games = models.Games.from_dict(data_dict=result)
            return games[0]

    """
    Matches
    -------
    """

    async def save_match(self, match: models.NewMatch, dry_run: bool = False) -> models.NewMatchResponse:
        """
        To save a match pass in the following parameters:
        :params models.NewMatch match: Completed new match model.
        :params bool dry_run: For testing, allows for debugging without actually saving the match or using any of the groups Quota.
        """
        params: dict[str, Union[str, int]] = {}
        if dry_run:
            params = {"dryrun": "true"}
        async with self._api as api:
            result = await api.request(endpoint=Endpoint.MATCH, json=match.as_dict(), params=params)
            return models.NewMatchResponse(**result)

    async def get_match_status(self) -> models.MatchStatus:
        """Get the status of matches posted by the API."""
        async with self._api as api:
            status_response = await api.request(endpoint=Endpoint.MATCH_STATUS)
            return models.MatchStatus(**status_response)

    async def get_all_matches(self) -> models.Matches:
        """Get all Matches from the group."""
        async with self._api as api:
            matches_response = await api.request(endpoint=Endpoint.MATCHES)
            return models.Matches.from_dict(data_dict=matches_response)

    async def get_match_with_id(self, id: str) -> Optional[models.Match]:
        """
        Get a match from the group with an Id matching the parameter.
        :param str id: Match Id to find.
        """
        matches = await self.get_all_matches()
        match = [m for m in matches if m.id == id]
        return match[0] if match else None

    async def get_matches_with_players(self, player_ids: MutableSequence[str]) -> Optional[models.Matches]:
        """
        Get Matches player by players matching Id's matching the parameter.
        :param: MutableSequence[str] player_ids: Id's of players to find matches they've player.
        """
        all_matches = await self.get_all_matches()
        filtered_matches = [m for m in all_matches if any(id in m.player_ids for id in player_ids)]
        return models.Matches(data=filtered_matches, totalMatches=len(filtered_matches))

    async def get_match_number(self, number: int) -> Optional[models.Match]:
        """
        Get match by number matching parameter.
        :param int number: Match number to find.
        """
        matches = await self.get_all_matches()
        match = [m for m in matches if m.number == number]
        return match[0] if match else None

    """
    Players
    """

    async def get_all_players(self) -> models.Players:
        """Get a list of all the players in the group."""
        async with self._api as api:
            players_response = await api.request(endpoint=Endpoint.PLAYERS)
            return models.Players(**players_response)

    async def new_ghost_player(self, name: str) -> models.Player:
        """
        Make a new ghost player to add to the group.
        There is a limit on Ghost users see [Quotas and Limits](https://rankade.com/api/#quota-and-limits).
        """
        assert isinstance(name, str)
        async with self._api as api:
            params: PARAMS = {"name": name}
            ghost_response = await api.request(endpoint=Endpoint.PLAYER, params=params)
            return models.Players.from_dict(data_dict=ghost_response)[0]

    """
    Quota
    """

    async def get_quota(self) -> models.Quota:
        """Returns current quota usage percentage"""
        async with self._api as api:
            quota_response = await api.request(endpoint=Endpoint.QUOTA)
            return models.Quota(**quota_response)

    """
    Rankings
    """

    async def get_rankings(
        self, subset_id: Optional[str] = None, match_number: Optional[int] = None
    ) -> models.Rankings:
        """Retrieve group's ranking for selected subset after the selected match number.
        :param subset_id: Id of the subset to be used.
        :param match_number: Retrieve subset results starting at match number provided.
        """
        assert isinstance(subset_id, (str, type(None)))
        assert isinstance(match_number, (int, type(None)))
        async with self._api as api:
            ranking_response = await api.request(endpoint=Endpoint.RANKINGS, subset=subset_id, match=match_number)
            return models.Rankings.from_dict(data_dict=ranking_response)

    """
    Subsets
    """

    async def get_subset_with_id(self, id: str) -> Optional[models.Subset]:
        """Return a specific subset using it's Id."""
        subsets = await self.get_subsets()
        subset = [s for s in subsets if s.id == id]
        return subset[0] if subset else None

    async def get_subsets(self) -> models.Subsets:
        """Return a list of all of a groups subsets."""
        async with self._api as api:
            subsets_attributes = await api.request(endpoint=Endpoint.SUBSET)
            return models.Subsets.from_dict(data_dict=subsets_attributes)
