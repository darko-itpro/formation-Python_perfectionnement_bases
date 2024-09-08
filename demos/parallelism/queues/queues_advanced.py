import time

import pya.concurrency.logger_conf

import logging
import threading
import queue
from random import randint
from time import sleep

buffer = queue.Queue()

orders = [("Meal 1", 9),
          ("Meal 2", 5),
          ("Meal 3", 4),
          ("Meal 4", 3),
          ("Meal 5", 7),
          ("Meal 6", 5),
          ]

class Cook(threading.Thread):
    def __init__(self, buffer):
        super().__init__(daemon=True)
        self.buffer = buffer
        self.product = None
        self.progress = 0
        self.working = False
        self.duration = 0

    @property
    def state(self):
        if self.working:
            return f"{self.product} ({self.progress}%)"
        return ":zzz: Idle"

    def run(self):
        while True:
            logging.info("Ready for work")
            self.product, self.duration = self.buffer.get()
            logging.info(f"Got {self.product}")
            self.simulate_cook()
            self.buffer.task_done()
            #self.simulate_idle()

    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))
        logging.info("waiting…")

    def simulate_cook(self):
        self.working = True
        self.progress = 0
        logging.info(f"Starting cooking for {self.product} by {self}")
        for _ in range(self.duration):
            sleep(1)
            self.progress += (1 / self.duration) * 100
        logging.info(f"Cooking for {self.product} done")


for product in orders[:4]:
    buffer.put(product)

Cook(buffer).start()
Cook(buffer).start()

#cook2.start()

for product in orders[4:]:
    buffer.put(product)
    sleep(1)



buffer.join()
#cook2.join()

print('All done')