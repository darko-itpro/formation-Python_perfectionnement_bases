"""
Démonstration des threads 01

Premier exemple sans threads, la durée est la durée totale.
"""

import demos.parallelism.logger_conf
import logging
import time

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish:str, duration:int):
    logging.info(f"Cooking {dish} started")
    time.sleep(duration)
    logging.info(f"Cooking {dish} done")

logging.info("Main    : before cooking")
start_time = time.time()

logging.info("Main    : cooking started")
cooking(*pasta)
cooking(*meat)

end_time = time.time()
logging.info(f"Main    : Collecting after {end_time - start_time:.2f} seconds, ready to serve")
