import asyncio
import random
import time

async def some_work(name):
    print(f'Started {name} ...')
    delay = random.uniform(0, 1.5)
    await asyncio.sleep(delay)
    print(f'... and finished {name} after {delay:.2f} seconds')

async def main():
    tasks = []
    for i in range(5):
        tasks.append(some_work(i))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    duration = time.time() - start
    print(f"Total duration: {duration}")
