import asyncio
import random

async def some_work(name):
    print(f'Started {name} ...')
    delay = random.uniform(0, 1.5)
    await asyncio.sleep(delay)
    print(f'... and finished {name}')


if __name__ == '__main__':
    asyncio.run(some_work("main"))

# Historically, now deprecated :
# loop = asyncio.get_event_loop()
# loop.run_until_complete("main")
