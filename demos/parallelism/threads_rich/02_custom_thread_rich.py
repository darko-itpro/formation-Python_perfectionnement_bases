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

    @property
    def duration(self):
        return self._duration

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

    console.clear()
    console.rule("Starting…")

    console.log("Main    : before creating thread")
    start_time = time.time()

    console.log("Main    : cooking started")

    burner1.cook(*pasta)
    burner2.cook(*meat)

    console.print()
    console.rule("Progress…")
    with Progress() as progress:
        progress1 = progress.add_task(f"[red]Cooking {burner1.dish}...", total=burner1.duration)
        progress2 = progress.add_task(f"[red]Cooking {burner2.dish}...", total=burner2.duration)


        while not progress.finished:
            progress.update(progress1, advance=1)
            progress.update(progress2, advance=1)
            time.sleep(1)

    console.log("Main    : processing done")

    console.print()
    console.rule("Processing done")
    burner1.join()
    burner2.join()
    end_time = time.time()
    console.print(f"Main    : Collecting after [bold]{end_time - start_time} seconds[/bold], ready to serve")
