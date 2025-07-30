"""
Démonstration des threads 04

Quatrième exemple avec les threads, problème de concurrence.
"""

import demos.parallelism.logger_conf
import logging
import threading
import time

from concurrent.futures import ThreadPoolExecutor

class Oven:
    def __init__(self):
        self._dish: str | None = None
        self._lock = threading.Lock()

    def cook_meal(self, dish: str, duration: int):
        logging.info("Ready to cook %s", dish)

        with self._lock:
            logging.info("Putting %s into oven", dish)
            self._dish = dish
            time.sleep(duration)
            logging.info("Taking out %s from oven", self._dish)


if __name__ == '__main__':
    pastry_01 = ("Bred", 8)
    pastry_02 = ("Cake", 4)

    oven = Oven()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(oven.cook_meal, *pastry_01)
        executor.submit(oven.cook_meal, *pastry_02)
