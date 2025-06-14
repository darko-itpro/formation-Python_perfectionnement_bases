"""
Démonstration des threads 02 bis

Second exemple bis avec les threads, basé sur
"""

import demos.parallelism.logger_conf
import logging
import threading
import time
from rich.console import Console
from rich.progress import Progress

pasta = ("pasta", 9)
meat = ("steak", 4)

class Burner(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)

        self._dish:str|None = None
        self._duration:int = 0

        self._reset_burner()

    @property
    def dish(self):
        return self._dish

    def _reset_burner(self):
        self._dish = None
        self._duration = 0

    def cook(self, dish:str, duration:int):
        self._dish = dish
        self._duration = duration

        self.start()

    def run(self):
        if self._dish is not None:
            for iteration in range(self._duration):
                time.sleep(1)

            self._reset_burner()


if __name__ == "__main__":
    burner1 = Burner()
    burner2 = Burner()

    console = Console()

    console.log("Main    : before creating thread")
    start_time = time.time()

    console.log("Main    : cooking started")

    with Progress() as progress:
        progress1 = progress.add_task(f"[red]Cooking {burner1.dish}...", total=100)
        progress2 = progress.add_task(f"[red]Cooking {burner2.dish}...", total=100)

        burner1.cook(*pasta)
        burner2.cook(*meat)

        while not progress.finished:
            



    burner1.join()
    burner2.join()
    end_time = time.time()
    console.log(f"Main    : Collecting after {end_time - start_time} seconds, ready to serve")
