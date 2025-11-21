import demos.parallelism.logger_conf
import logging
import time

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish:str, duration:int):
    logging.info("Cooking %s started", dish)
    time.sleep(duration)
    logging.info("Cooking %s done", dish)

if __name__ == "__main__":
    logging.info("Main    : before cooking")
    start_time = time.time()

    logging.info("Main    : cooking started")
    cooking(*pasta)
    cooking(*meat)

    end_time = time.time()
    logging.info("Main    : Collecting after %.2f seconds, ready to serve", end_time - start_time)
