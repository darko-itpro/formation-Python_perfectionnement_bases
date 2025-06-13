"""
Démonstration des threads 04

Quatrième exemple avec les threads, problème de concurrence.
"""

import demos.parallelism.logger_conf
import logging
import threading
import time


class Oven:
    def __init__(self):
        self._dish:str|None = None
        self._lock = threading.Lock()

    def cook_meal(self, dish:str, duration:int):
        logging.info("Ready to cook %s", dish)

        with self._lock:
            #self._lock.acquire()
            logging.info("Putting %s into oven", dish)
            self._dish = dish
            time.sleep(duration)
            logging.info("Taking out %s from oven", self._dish)
            #self._lock.release()

if __name__ == '__main__':
    pastry_01 = ("Bred", 8)
    pastry_02 = ("Cake", 4)

    oven = Oven()

    bread_cooker = threading.Thread(target=oven.cook_meal, args=pastry_01)
    cake_cooker = threading.Thread(target=oven.cook_meal, args=pastry_02)

    bread_cooker.start()
    cake_cooker.start()
