"""
Démonstration des threads 05

Exemple d'utilisation de semaphore, created by Edsger W. Dijkstra
"""

import demos.parallelism.logger_conf
import logging
import threading
import time
import random

menu = [
    ("Burger with fries", 8),
    ("Hot Dog", 5),
    ("Pizza Napolitana", 4),
    ("Fish and chips", 7),
    ("Venison Stew", 10),
]

class KitchenTeam:
    def __init__(self, team=4):
        self._team = threading.Semaphore(value=team)

    def cook(self, dish, duration):
        with self._team:
            logging.info("Order %s started, ready in %d.", dish, duration)
            time.sleep(duration)
            logging.info("%s cooked", dish)

kitchen = KitchenTeam(4)

kitchen_open = True
max = 5
available_orders = random.randint(40, 60)
while available_orders:
    # Picking one random menu item to simulate an order
    new_client_order = random.choice(menu)
    logging.info("sending order %s", new_client_order[0])
    in_process = threading.Thread(target=kitchen.cook, args=new_client_order)
    in_process.start()

    # Random sleep between clients
    wait_time = random.randint(0, 5)
    time.sleep(wait_time)

    available_orders -= 1
    if not available_orders:
        logging.warning("Last order sent, kitchen closing")