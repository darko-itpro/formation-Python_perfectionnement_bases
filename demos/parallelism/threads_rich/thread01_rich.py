"""
Démonstration des threads 01

Premier exemple sans threads, la durée est la durée totale.
"""

import demos.parallelism.logger_conf
import logging
import time
from rich.console import Console

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish:str, duration:int):
    console.log(f"Cooking {dish} started")
    time.sleep(duration)
    console.log(f"Cooking {dish} done")


console = Console()
with (console.status("[bold green]Cooking will start...[/bold green]", spinner="aesthetic")
      as status):
    time.sleep(1)
    start_time = time.time()

    status.update(f"[bold green]Cooking {pasta[0]}[/bold green]")
    cooking(*pasta)
    status.update(f"[bold green]Cooking {meat[0]}[/bold green]")
    cooking(*meat)

end_time = time.time()
console.print(f"Main    : Collecting after {end_time - start_time:.2f} seconds, ready to serve")
