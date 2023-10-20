import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())