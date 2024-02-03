# rankade.Rankade.py
from __future__ import annotations

import logging
from contextlib import AbstractAsyncContextManager
from types import TracebackType
from typing import MutableSequence, Optional, Type, Union

import aiohttp

import rankade.models as models
from rankade.api import Api, Endpoint
from rankade.api.Api import PARAMS

logger: logging.Logger = logging.getLogger(__name__)


class Rankade(AbstractAsyncContextManager["Rankade"]):
    """Main wrapper around the Rankade Api. Use this class along with it's methods to access the Api.
    It is generally best to use this as a context manager as it will manage the creation and cleanup of the ClientSession.

    ```python
        async with Rankade(...) as rank:
            result = rank.request(...)
    ```
    It can also be used without the context manager, if you are managing the ClientSession & error handling yourself.

    ```python
        rank = rankade(...)
        async rank.start()
        async rank.request(...)
        ...
        async rank.stop()
    ```

    """

    def __init__(
        self,
        key_or_token: str,
        secret: Optional[str] = None,
        base_url: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ):
        self._session = session
        self._api = Api(key_or_token, secret, base_url=base_url, session=session)

    async def start(self) -> None:
        """
        :::{versionadded} 0.2.0
        :::
        Creates a Client session if none was passed through.

        :::{note}
        Should only be called manually if not using Rankade as a context manager.
        :::
        """
        logger.debug("Context started.")
        if self._session is None or self._session.closed:
            logger.debug("Creating ClientSession.")
            self._session = aiohttp.ClientSession()

    async def stop(self) -> None:
        """
        :::{versionadded} 0.2.0
        :::
        Closes the Client session.

        :::{note}
        Should only be called manually if not using Rankade as a context manager.
        :::

        """
        logger.debug("Context finishing.")
        if self._session:
            logger.debug("Closing ClientSession.")
            await self._session.close()

    """
    Games
    """

    async def get_games(self) -> models.Games:
        """Returns the list of the group's games (i.e. games with at least one match played within the group)."""

        games_response = await self._api.request(endpoint=Endpoint.GAMES)
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
        search_endpoint = Endpoint.GAMES_SEARCH
        params: PARAMS = {"name": name}
        games_response = await self._api.request(endpoint=search_endpoint, params=params)
        return models.Games.from_dict(data_dict=games_response)

    async def new_game_with_bggId(self, bggId: int) -> models.Game:
        """Add a new game by [Board Game Geek)[https://boardgamegeek.com/] ID."""
        params: PARAMS = {"bggId": bggId}
        return await self._new_game_with(params=params)

    async def new_game_with_name(self, name: str) -> models.Game:
        """Add a new game by name."""
        params: PARAMS = {"name": name}
        return await self._new_game_with(params=params)

    async def _new_game_with(self, params: PARAMS) -> models.Game:
        result = await self._api.request(endpoint=Endpoint.GAME, params=params)
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
        params: PARAMS = {}
        if dry_run:
            params["dryrun"] = "true"
        result = await self._api.request(endpoint=Endpoint.MATCH, json=match.as_dict(), params=params)
        return models.NewMatchResponse(**result)

    async def get_match_status(self) -> models.MatchStatus:
        """Get the status of matches posted by the API."""
        status_response = await self._api.request(endpoint=Endpoint.MATCH_STATUS)
        return models.MatchStatus(**status_response)

    async def get_all_matches(self) -> models.Matches:
        """Get all Matches from the group."""
        matches_response = await self._api.request(endpoint=Endpoint.MATCHES)
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
        players_response = await self._api.request(endpoint=Endpoint.PLAYERS)
        return models.Players.from_dict(data_dict=players_response)

    async def new_ghost_player(self, name: str) -> models.Player:
        """
        Make a new ghost player to add to the group. [What is a ghost user](https://rankade.com/frequently-asked-question/3/what-is-a-ghost-user/67)
        There is a limit on Ghost users see [Quotas and Limits](https://rankade.com/api/#quota-and-limits).
        """
        params: PARAMS = {"name": name}
        ghost_response = await self._api.request(endpoint=Endpoint.PLAYER, params=params)
        return models.Players.from_dict(data_dict=ghost_response)[0]

    """
    Quota
    """

    async def get_quota(self) -> models.Quota:
        """Returns current quota usage percentage"""
        quota_response = await self._api.request(endpoint=Endpoint.QUOTA)
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
        ranking_response = await self._api.request(endpoint=Endpoint.RANKINGS, subset=subset_id, match=match_number)
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
        subsets_attributes = await self._api.request(endpoint=Endpoint.SUBSET)
        return models.Subsets.from_dict(data_dict=subsets_attributes)

    async def __aenter__(self) -> Rankade:
        """
        :::{versionadded} 0.2.0
        :::
        Entry handler for context manager.
        """
        await self.start()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Union[bool, None]:
        """
        :::{versionadded} 0.2.0
        :::
        Cleanup handler for context manager.
        """
        # Do not return 'True' here or exceptions will be supressed.
        # https://docs.python.org/3/reference/datamodel.html?#object.__exit__
        await self.stop()
