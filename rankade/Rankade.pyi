"""
This type stub file was generated by pyright.
"""

import logging
from contextlib import AbstractAsyncContextManager
from types import TracebackType
from typing import MutableSequence, Optional, Type, Union

import aiohttp

import rankade.models as models

logger: logging.Logger = ...

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
        secret: Optional[str] = ...,
        base_url: Optional[str] = ...,
        session: Optional[aiohttp.ClientSession] = ...,
    ) -> None: ...
    async def start(self) -> None:
        """
        :::{versionadded} 0.2.0
        :::
        Creates a Client session if none was passed through.

        :::{note}
        Should only be called manually if not using Rankade as a context manager.
        :::
        """
        ...

    async def stop(self) -> None:
        """
        :::{versionadded} 0.2.0
        :::
        Closes the Client session.

        :::{note}
        Should only be called manually if not using Rankade as a context manager.
        :::

        """
        ...

    async def get_games(self) -> models.Games:
        """Returns the list of the group's games (i.e. games with at least one match played within the group)."""
        ...

    async def get_popular_games(self) -> models.Games:
        """
        Not implemented on server, is in API documentation, but requests return an error.

        :raises: NotImplementedError
        """
        ...

    async def game_search(self, name: str) -> models.Games:
        """
        Searches games by name.

        :param name: Name of game to be searched for
        """
        ...

    async def new_game_with_bggId(self, bggId: int) -> models.Game:
        """Add a new game by [Board Game Geek)[https://boardgamegeek.com/] ID."""
        ...

    async def new_game_with_name(self, name: str) -> models.Game:
        """Add a new game by name."""
        ...

    async def save_match(self, match: models.NewMatch, dry_run: bool = ...) -> models.NewMatchResponse:
        """
        To save a match pass in the following parameters:
        :params models.NewMatch match: Completed new match model.
        :params bool dry_run: For testing, allows for debugging without actually saving the match or using any of the groups Quota.
        """
        ...

    async def get_match_status(self) -> models.MatchStatus:
        """Get the status of matches posted by the API."""
        ...

    async def get_all_matches(self) -> models.Matches:
        """Get all Matches from the group."""
        ...

    async def get_match_with_id(self, id: str) -> Optional[models.Match]:
        """
        Get a match from the group with an Id matching the parameter.
        :param str id: Match Id to find.
        """
        ...

    async def get_matches_with_players(self, player_ids: MutableSequence[str]) -> Optional[models.Matches]:
        """
        Get Matches player by players matching Id's matching the parameter.
        :param: MutableSequence[str] player_ids: Id's of players to find matches they've player.
        """
        ...

    async def get_match_number(self, number: int) -> Optional[models.Match]:
        """
        Get match by number matching parameter.
        :param int number: Match number to find.
        """
        ...

    async def get_all_players(self) -> models.Players:
        """Get a list of all the players in the group."""
        ...

    async def new_ghost_player(self, name: str) -> models.Player:
        """
        Make a new ghost player to add to the group. [What is a ghost user](https://rankade.com/frequently-asked-question/3/what-is-a-ghost-user/67)
        There is a limit on Ghost users see [Quotas and Limits](https://rankade.com/api/#quota-and-limits).
        """
        ...

    async def get_quota(self) -> models.Quota:
        """Returns current quota usage percentage"""
        ...

    async def get_rankings(self, subset_id: Optional[str] = ..., match_number: Optional[int] = ...) -> models.Rankings:
        """Retrieve group's ranking for selected subset after the selected match number.
        :param subset_id: Id of the subset to be used.
        :param match_number: Retrieve subset results starting at match number provided.
        """
        ...

    async def get_subset_with_id(self, id: str) -> Optional[models.Subset]:
        """Return a specific subset using it's Id."""
        ...

    async def get_subsets(self) -> models.Subsets:
        """Return a list of all of a groups subsets."""
        ...

    async def __aenter__(self) -> Rankade:
        """
        :::{versionadded} 0.2.0
        :::
        Entry handler for context manager.
        """
        ...

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
        ...
