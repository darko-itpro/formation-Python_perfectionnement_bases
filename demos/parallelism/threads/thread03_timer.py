"""
Third example delaying a thread with timer.
"""

import demos.parallelism.logger_conf
import logging
import threading
import time

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish, duration):
    logging.info(f"Cooking {dish} started")
    time.sleep(duration)
    logging.info(f"Cooking {dish} done")

logging.info("Main    : before creating thread")
start_time = time.time()
logging.info("Main    : wait for our cooking to finish")

pasta_cook = threading.Thread(target=cooking, args=pasta)
meat_cook = threading.Timer(pasta[1] - meat[1], cooking, args=meat)

logging.info("Main    : before running thread")
pasta_cook.start()
meat_cook.start()

pasta_cook.join()
meat_cook.join()

end_time = time.time()

logging.info(f"Main    : Collecting after {end_time - start_time:.2f} seconds, ready to serve")
