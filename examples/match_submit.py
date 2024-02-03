import asyncio
import os

import rankade
from rankade.models import Faction, NewMatch, Players

"""
Either set RANKADE_KEY & RANKADE_SECRET environmental variables to the
appropriate values or replace ```key = os.getenv("RANKADE_KEY", "")```
with ```key = "your rankade api key"```.
"""


async def main():
    key = os.getenv("RANKADE_KEY", "")
    secret = os.getenv("RANKADE_SECRET", "")
    async with rankade.Rankade(key_or_token=key, secret=secret) as rankade_api:
        games = await rankade_api.game_search("Twilight Imperium")
        print(games[0])
        """
        Game(
            id=962,
            name='Twilight Imperium (Third Edition)',
            weight='normal',
            weightLabel='Normal',
            mediumImage='https://userscontents.rankade.com/images/500/...',
            thumbnail='https://cf.geekdo-images.com/thumb/img/...',
            bggIdGame=12493
        )
        """

        match = NewMatch(game=games[0], notes="", weight="normal")

        players = await rankade_api.get_all_players()
        print(players)
        """
        Players(data=
        Player(
            id="Dwog3w8mgAL",
            ghost=1,
            username="",
            displayName="*LongJohn",
            icon="",),
        Player(
            id="JVk1OklO1ov",
            ghost=1,
            username="",
            displayName="*Captain Nemo",
            icon="",
        ))
        """

        """
        Players can be added to factions in a couple of ways.
        Either we can grabbing the player directly from the list
        of all players and calling the add_faction method of NewMatch
        """
        match.add_faction(players[0], rank=1, points="31")

        """
        Or we can manually create the faction with by calling the Faction
        class and appending the faction to the list of factions.
        """
        player_2 = Players(data=[players[1]])
        faction = Faction(players=player_2, rank=2, points="21", name="")
        match.factions.append(faction)

        """
        Finally we can save the new match, any errors in server side
        validation will be raised as exceptions.
        """
        results = await rankade_api.save_match(match)
        print(results)


if __name__ == "__main__":
    asyncio.run(main())
