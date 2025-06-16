import demos.parallelism.logger_conf
import logging
import asyncio
import random
import time

async def some_work(name):
    logging.info('Started %s ...', name)
    delay = random.uniform(0, 1.5)
    await asyncio.sleep(delay)
    logging.info('... and finished %s after %.2f seconds', name, delay)

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i in range(5):
            tasks.append(tg.create_task(some_work(i)))



if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    duration = time.time() - start
    logging.info("Total duration: %.2f", duration)
