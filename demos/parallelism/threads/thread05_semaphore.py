"""
Démonstration des threads 05

Exemple d'utilisation de semaphore
"""
from contextlib import closing

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
            logging.info(f"Order {dish} started, ready in {duration}.")
            time.sleep(duration)
            logging.info(f"{dish} cooked")

kitchen = KitchenTeam(4)

kitchen_open = True
max = 5
available_orders = random.randint(40, 60)
while available_orders:
    # Picking one random menu item to simulate an order
    new_client_order = random.choice(menu)
    logging.info(f"sending order {new_client_order[0]}")
    in_process = threading.Thread(target=kitchen.cook, args=new_client_order)
    in_process.start()

    # Random sleep between clients
    wait_time = random.randint(0, 5)
    time.sleep(wait_time)

    # Chaos addition
    if wait_time == max and wait_time > 1: max -= 1
    if wait_time == 0: max += 1
    available_orders -= 1
    if not available_orders:
        logging.warning("Last order sent, kitchen closing")