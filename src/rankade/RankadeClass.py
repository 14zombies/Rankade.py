# Rankade.py
from asyncio import AbstractEventLoop

from dataclasses import dataclass
from typing import List, Optional

import rankade.api as api
import rankade.models as models
from rankade.api import Endpoint
from .Consts import *


class Rankade(object):

    def __init__(self, key_or_token: str, secret: Optional[str] = None, base_url: Optional[str] = None, loop: Optional[AbstractEventLoop] = None):
        self._api = api.Api(
            key_or_token, secret, base_url=base_url, loop=loop)

#
# Games
#
    async def __aenter__(self) -> "Rankade":
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self._api.close()

    async def get_games(self) -> models.Games:
        games_response = await self._api.request(endpoint=Endpoint.GAMES)
        return models.Games(self._api, games_response)

    async def get_popular_games(self) -> models.Games:
        """Not implimented on server, is in Api documentation,
        but requests return an error."""
        raise NotImplementedError("Not implimented on server, request returns an error.")
        # If ever gets implimented on server this should be uncommented.
        # games_attributes = await self._api.get(Endpoint.POPULAR)
        # return models.Games(self._api, games_attributes)

    async def game_search(self, name: str) -> models.Games:
        assert isinstance(name, str)
        search_endpoint = Endpoint.SEARCH_GAMES
        search_endpoint.add_paramater("name", name)
        games_response = await self._api.request(search_endpoint)
        return models.Games(self._api, games_response)

#
# Matches
#
    def new_match(self, game: models.Game, notes: str) -> models.Match:
        assert isinstance(game, models.Game)
        assert isinstance(notes, str)
        return models.Match(self._api,
                            weight=game.weight,
                            weightLabel=game.weightLabel,
                            game=game.__dict__,
                            notes=notes,
                            factions=[]
                            )

    async def get_match_status(self) -> models.MatchStatus:
        status_response = await self._api.request(Endpoint.MATCH_STATUS)
        return models.MatchStatus(self._api, **status_response)

    async def get_all_matches(self) -> models.Matches:
        matches_response = await self._api.request(Endpoint.MATCHES)
        return models.Matches(self._api, **matches_response)

    async def get_match_with_id(self) -> Optional[models.Match]:
        pass

    async def get_matches_with_players(self, player_ids: List[str]) -> models.Matches:
        return models.Matches(None, None, 0, 0, 0, 0)

    async def get_match_number(self, number) -> Optional[models.Match]:
        pass

#
#  Players
#
    async def get_all_players(self) -> models.Players:
        players_response = await self._api.request(Endpoint.PLAYERS)
        return models.Players(self._api, **players_response)

    async def new_ghost_player(self, name: str) -> models.Player:
        assert isinstance(name, str)
        ghost_endpoint = Endpoint.PLAYER
        ghost_endpoint.add_paramater("name", name)
        ghost_response = await self._api.request(ghost_endpoint)
        return models.Player(self._api, **ghost_response)

#
# Quota
#
    async def get_quota(self) -> models.Quota:
        quota_response = await self._api.request(endpoint=Endpoint.QUOTA)
        return models.Quota(self._api, **quota_response)

#
# Rankings
#
    async def get_rankings(self, subset_id: Optional[str] = None, match_number: Optional[int] = None) -> models.Rankings:
        assert isinstance(subset_id, (str, type(None)))
        assert isinstance(match_number, (int, type(None)))
        ranking_endpoint = Endpoint.RANKINGS
        # params = ["rankings"]
        # if isinstance(subset_id, str):
        #     params.append(subset_id)
        # if isinstance(match_number, int):
        #     params.append(str(match_number))
        # else:
        #     params.append("last")
        # if isinstance(page, int):
        #     params.append(str(page))
        # else:
        #     params.append("1")
        # endpoint = "/".join(params)

        ranking_response = await self._api.request(ranking_endpoint)
        return models.Rankings(self._api, **ranking_response)

#
# Subsets
#
    async def get_subset_with_id(self, id) -> Optional[models.Subset]:
        assert isinstance(id, (str, type(None)))
        pass

    async def get_all_subsets(self) -> models.Subsets:
        subsets_attributes = await self._api.request(Endpoint.SUBSET)
        return models.Subsets(self._api, subsets_attributes)
