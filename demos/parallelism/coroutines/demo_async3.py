import demos.parallelism.logger_conf
import logging
import asyncio
import random
import time

async def some_work(name):
    logging.info('Started %s ...', name)
    delay = random.uniform(1, 2.5)
    await asyncio.sleep(delay)
    logging.info('... and finished %s after %.2f seconds', name, delay)

async def main():
    t1 = asyncio.create_task(some_work("Premier"))
    t2 = asyncio.create_task(some_work("Deuxième"))
    t3 = asyncio.create_task(some_work("Troisième"))
    t4 = asyncio.create_task(some_work("Obi Wan Kenobi"))
    t5 = asyncio.create_task(some_work("Cinquième"))

    await t1
    await t2
    await t3
    await t4
    await t5


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    duration = time.time() - start
    logging.info("Total duration: %.2f", duration)
