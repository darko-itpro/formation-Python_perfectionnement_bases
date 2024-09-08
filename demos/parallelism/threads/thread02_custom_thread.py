"""
Démonstration des threads 02 bis

Second exemple bis avec les threads, basé sur
"""

import demos.parallelism.logger_conf
import logging
import threading
import time

pasta = ("pasta", 9)
meat = ("steak", 4)

class Burner(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self._reset_burner()

    def _reset_burner(self):
        self._dish = None
        self._duration = 0

    def cook(self, dish, duration):
        self._dish = dish
        self._duration = duration

        self.start()

    def run(self):
        if self._dish is not None:
            logging.info(f"Cooking {self._dish} started")
            time.sleep(self._duration)
            logging.info(f"Cooking {self._dish} done")

            self._reset_burner()


logging.info("Main    : before creating thread")
start_time = time.time()
logging.info("Main    : wait for our cooking to finish")

burner1 = Burner()
burner2 = Burner()

logging.info("Main    : before running thread")
burner1.cook(*pasta)
burner2.cook(*meat)

burner1.join()
burner2.join()
end_time = time.time()
logging.info(f"Main    : Collecting after {end_time - start_time:.2f} seconds, ready to serve")
