# Rankade.py
import json
import logging

import rankade.Api
import rankade.Game
import rankade.Games
import rankade.Match
import rankade.MatchStatus
import rankade.Player
import rankade.Players
import rankade.Quota
import rankade.Rankings
import rankade.Subsets

from . import RankadeExceptions
from .Consts import *


class Rankade(object):

    def __init__(self, key_or_token=None, secret=None, base_url=DEFAULT_BASE_URL, loop=None):
        self._api = rankade.Api.Api(key_or_token, secret, base_url=base_url, loop=loop)

#
# Games
#

    async def get_games(self):
        endpoint = "games"
        games_attributes = await self._api.get(endpoint=endpoint)
        games = rankade.Games.Games(self._api, games_attributes)
        return games.content

    async def get_popular_games(self):
        pass
        # Not implimented for some reason.
        # endpoint = "games/popular"
        # games_attributes = await self._api.get(endpoint=endpoint)
        # games = rankade.Games.Games(self._api, games_attributes)
        # return games.content

    async def game_search(self, name: str) -> list:
        if len(name) < 2:
            raise RankadeExceptions.SearchTooShort(search=name)

        endpoint = "games/search"
        params = {'name': name}
        games_attributes = await self._api.get(endpoint=endpoint,
                                               params=params
                                               )
        games = rankade.Games.Games(self._api, games_attributes)
        if len(games.content) == 0:
            logging.info("No results found for game named {}".format(name))

        return games.content

#
# Matches
#
    def new_match(self, game: rankade.Game.Game, notes: str):
        if DRYRUN:
            params = {"dryrun": DRYRUN}
        else:
            params = {}
        match_attributes = {
            "id": None,
            "externalId": None,
            "date": None,
            "registrationDate": None,
            "number": None,
            "summary": None,
            "matchType": None,
            "draw": None,
            "weight": game.weight,
            "weightLabel": "",
            "game": game.__dict__,
            "factions": None,
            "notes": notes
        }

        return rankade.Match.Match(self._api, match_attributes)

    async def get_match_status(self) -> rankade.MatchStatus.MatchStatus:
        endpoint = "matches/status"
        status_attributes = await self._api.get(endpoint=endpoint)
        status = rankade.MatchStatus.MatchStatus(self._api, status_attributes)
        return status


#
#  Players
#
    async def get_all_players(self) -> list:
        first_page = await self.get_players_page()
        players = first_page.content
        next_page = await first_page.next_page()
        while next_page is not None:
            players += next_page.content
            next_page = await next_page.next_page()
        return players

    async def get_players_page(self, page: int = 1) -> rankade.Players.Players:
        response = await self._api.get(endpoint="players/{}".format(page))
        return rankade.Players.Players(self._api, response)

#
# Quota
#
    async def get_quota(self):
        endpoint = "quota"
        quota_attributes = await self._api.get(endpoint=endpoint)
        return rankade.Quota.Quota(self._api, quota_attributes)

#
# Rankings
#
    async def get_rankings(self, subset_id=None, match_number=None, page=None):
        params = ["rankings"]
        if isinstance(subset_id, str):
            params.append(subset_id)
        if isinstance(match_number, int):
            params.append(str(match_number))
        else:
            params.append("last")
        if isinstance(page, int):
            params.append(str(page))
        else:
            params.append("1")
        endpoint = "/".join(params)

        ranking_attributes = await self._api.get(endpoint)
        return rankade.Rankings.Rankings(self._api, ranking_attributes)

#
# Subsets
#
    async def get_all_subsets(self):
        endpoint = "subsets"
        subsets_attributes = await self._api.get(endpoint)
        return rankade.Subsets.Subsets(self._api, subsets_attributes)
