import asyncio
import os

import rankade

"""
Either set RANKADE_KEY & RANKADE_SECRET environmental variables to the
appropriate values or replace ```key = os.getenv("RANKADE_KEY", "")```
with ```key = "your rankade api key"```.

"""


async def main():
    key = os.getenv("RANKADE_KEY", "")
    secret = os.getenv("RANKADE_SECRET", "")
    search_term = "Twilight Imperium"
    async with rankade.Rankade(key_or_token=key, secret=secret) as rankade_api:
        result = await rankade_api.game_search(name=search_term)
        print(result[0])

        """
        At the time of writing this would give the following output:

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


if __name__ == "__main__":
    asyncio.run(main())
