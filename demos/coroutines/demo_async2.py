import asyncio
import time

async def some_work(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await some_work(1, 'hello')
    await some_work(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())