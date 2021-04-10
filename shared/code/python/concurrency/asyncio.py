import asyncio
import time


async def work():
    print(f"started at {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"finished at {time.strftime('%X')}")


async def main():
    await asyncio.gather(work(), work())


asyncio.run(main())
