"""
Démonstration du passage au multiprocessing

Il s'agit de l'exemple avec les threads avec join afin d'illustrer la proximité de la syntaxe
du multiprocessing.
"""

import demos.parallelism.logger_conf
import logging
#from threading import Thread as Task
from multiprocessing import Process as Task
import time

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish:str, duration:int):
    logging.info("Cooking %s started", dish)
    time.sleep(duration)
    logging.info("Cooking %s done", dish)

if __name__ == "__main__":
    logging.info("Main    : before creating thread")
    start_time = time.time()
    logging.info("Main    : wait for our cooking to finish")

    pasta_cook = Task(target=cooking, args=pasta)
    meat_cook = Task(target=cooking, args=meat)

    logging.info("Main    : before running thread")
    pasta_cook.start()
    meat_cook.start()

    pasta_cook.join()
    meat_cook.join()

    end_time = time.time()
    logging.info("Main    : Collecting after %.2f seconds, ready to serve", end_time - start_time)
