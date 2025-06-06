import random

import demos.parallelism.logger_conf
import logging
import time
import threading
from concurrent.futures import ThreadPoolExecutor

import questionary


def file_downloader(path):
    logging.info(f"Downloading {path} started…")
    start = time.time()
    time_picked = random.randint(1, 5)
    time.sleep(time_picked)
    duration = time.time() - start
    logging.info(f"File {path} loaded in {duration:.2} seconds ({time_picked})")

def version_1():
    num_files = int(questionary.text("Combien de fichiers ?").ask())


    downloaders = []
    for i in range(num_files):
        t = threading.Thread(target=file_downloader, args=(f"File_{i:02}",))
        t.start()
        downloaders.append(t)

    for t in downloaders:
        t.join()
    print("Fini")

def version_pool():
    num_files = int(questionary.text("Combien de fichiers ?").ask())
    questionary.path('Quel fichier ?').ask()

    with ThreadPoolExecutor(max_workers=4, ) as executor:
        for i in range(num_files):
            executor.submit(file_downloader, (f"File_{i:02}",))

    print("Fini")


if __name__ == "__main__":
    start = time.time()
    version_pool()
