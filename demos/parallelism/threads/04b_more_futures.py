import demos.parallelism.logger_conf
import logging
import time

from concurrent.futures import ThreadPoolExecutor


pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish, duration):
    logging.info("Cooking %s started", dish)
    time.sleep(duration)
    logging.info("Cooking %s done", dish)

    return f"{dish} on plate"

if __name__ == "__main__":
    logging.info("Main    : before creating thread")
    start_time = time.time()

    order = []

    def serve(plate):
        order.append(plate.result())
        logging.info("Order done added to plate")

    logging.info("Main    : cooking started")
    with ThreadPoolExecutor(max_workers=2) as executor:
        ex1 = executor.submit(cooking, *pasta)
        ex2 = executor.submit(cooking, *meat)

        ex1.add_done_callback(serve)
        ex2.add_done_callback(serve)

    end_time = time.time()
    logging.info("Main    : Collecting after %.2f seconds, ready to serve : %s", end_time - start_time, order)
