from watchy import Watchy
from utils import vibrate_motor
import uasyncio as asyncio


# vibrate_motor([500])  # done


async def main():
    w = Watchy()


asyncio.run(main())
