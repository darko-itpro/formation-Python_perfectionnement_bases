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

        self._dish:str|None = None
        self._duration:int = 0

        self._reset_burner()

    def _reset_burner(self):
        self._dish = None
        self._duration = 0

    def cook(self, dish:str, duration:int):
        self._dish = dish
        self._duration = duration

        self.start()

    def run(self):
        if self._dish is not None:
            logging.info("Cooking %s started", self._dish)
            time.sleep(self._duration)
            logging.info("Cooking %s done", self._dish)

        self._reset_burner()


if __name__ == "__main__":
    burner1 = Burner()
    burner2 = Burner()

    logging.info("Main    : before creating thread")
    start_time = time.time()

    logging.info("Main    : cooking started")
    burner1.cook(*pasta)
    burner2.cook(*meat)

#    burner1.join()
#    burner2.join()
    end_time = time.time()
    logging.info("Main    : Collecting after %.2f seconds, ready to serve", end_time - start_time)
