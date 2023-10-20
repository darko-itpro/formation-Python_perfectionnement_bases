import asyncio
import random

async def big_work(msg):
    delay = random.uniform(0, 1.5)

    await asyncio.sleep(delay)
    print(f"{msg} done after {delay:.2f}")


async def main():
    tasks = []
    for i in range(5):

        tasks.append(big_work(i))
    await asyncio.gather(*tasks)
asyncio.run(main())

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())