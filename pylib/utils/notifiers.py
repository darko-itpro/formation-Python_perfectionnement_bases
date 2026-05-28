import random
import time
import logging
import pylib.settings

def make_notify(service_name: str, min_delay: float = 1, max_delay: float = 5):
    def notify():
        delay = random.uniform(min_delay, max_delay)
        logging.info(f"[{service_name}] starting (will take {delay:.2f}s)")
        time.sleep(delay)
        logging.info(f"[{service_name}] done")
    return notify
