"""
Démonstration des threads 05

Exemple d'utilisation de semaphore
"""

import demos.concurrency.logger_conf
import logging
import threading
import time
import random

class KitchenTeam:
    def __init__(self, team=4):
        self._team = threading.Semaphore(value=team)

    def cook(self, dish, duration=None):
        if not duration:
            duration = random.randint(5, 9)

        with self._team:
            logging.info(f"Cooking {dish} started for {duration} time")
            time.sleep(duration)
            logging.info(f"{dish} cooked")

kitchen = KitchenTeam(4)

for order in ("pizza", "kebab", "fish", "burger", "haggies", "fish and chips", "cake", "nuggets"):
    in_process = threading.Thread(target=kitchen.cook, args=(order,))
    in_process.start()
