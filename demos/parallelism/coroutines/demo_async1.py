import demos.parallelism.logger_conf
import logging
import asyncio
import random

async def some_work(name):
    logging.info('Started %s ...', name)
    delay = random.uniform(0, 1.5)
    await asyncio.sleep(delay)
    logging.info('... and finished %s ...', name)


if __name__ == '__main__':
    asyncio.run(some_work("main"))

# Historically, now deprecated :
# loop = asyncio.get_event_loop()
# loop.run_until_complete("main")
