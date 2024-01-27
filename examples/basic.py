import asyncio
import os

from rankade.Rankade import Rankade


async def main():
    # Example usage
    key = os.getenv("RANKADE_KEY", "")
    secret = os.getenv("RANKADE_Secret")

    rankade = Rankade(key_or_token=key, secret=secret)
    result = rankade.get_games()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
