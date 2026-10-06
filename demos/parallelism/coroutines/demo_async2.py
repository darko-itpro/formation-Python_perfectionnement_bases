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
    await some_work("Premier")
    await some_work("Second")
    await some_work("Troisième")
    await some_work("Obi Wan Kenobi")
    await some_work("Cinquième")


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    duration = time.time() - start
    logging.info("Total duration: %.2f seconds", duration)
