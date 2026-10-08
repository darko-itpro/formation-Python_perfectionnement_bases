import random
import time
import logging
import asyncio
import pylib.settings


def make_notify(service_name: str, min_delay: float = 1, max_delay: float = 5):
    def notify():
        delay = random.uniform(min_delay, max_delay)
        logging.info(f"[{service_name}] starting (will take {delay:.2f}s)")
        time.sleep(delay)
        print(f"Notification {service_name} sent")
        logging.info(f"[{service_name}] done")
    return notify

def make_async_notify(service_name: str, min_delay: float = 1, max_delay: float = 5):
    async def notify():
        delay = random.uniform(min_delay, max_delay)
        logging.info(f"[{service_name}] starting (will take {delay:.2f}s)")
        await asyncio.sleep(delay)
        print(f"Notification {service_name} sent")
        logging.info(f"[{service_name}] done")
    return notify
