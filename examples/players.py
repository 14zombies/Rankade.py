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
    secret = os.getenv("RANKADE_SECRET")

    rankade_api = rankade.Rankade(key_or_token=key, secret=secret)
    result = await rankade_api.get_all_players()
    print(result[0])


if __name__ == "__main__":
    asyncio.run(main())
