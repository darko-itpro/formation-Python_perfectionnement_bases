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
        self._dish = None
        self._lock = threading.Lock()

    def cook_meal(self, dish, duration):
        logging.info(f"Ready to cook {dish}")

        #with self._lock:
        #self._lock.acquire()
        logging.info(f"Putting {dish} into oven")
        self._dish = dish
        time.sleep(duration)
        logging.info(f"Taking out {self._dish} from oven")
        #self._lock.release()


meal1 = ("Bred", 8)
meal2 = ("Cake", 4)

oven = Oven()

bread_cooker = threading.Thread(target=oven.cook_meal, args=meal1)
cake_cooker = threading.Thread(target=oven.cook_meal, args=meal2)

bread_cooker.start()
cake_cooker.start()

# for _ in range(20):
#     print(f"{oven._dish} in the oven")
#     time.sleep(1)
