"""
Pour illustrer les queues, cet exemple possède une fonction "worker" dans un thread. Le worker
récupère un élément de la queue pour le traiter. La queue a une capacité limitée.

L'exemple montre que le programme principal s'arrête lorsque la queue est pleine et ne peut
remettre un élément que lorsqu'il est retiré de la queue.
"""

import threading
import queue
import time
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live

console = Console()
layout = Layout()

layout.split(
    Layout(name="header", size=1),
    Layout(name="main"),
)

layout["main"].split_row(Layout(name="task"), Layout(name="pipe", ratio=2))

q = queue.Queue(4)

def worker():

    while True:
        item = q.get()
        time.sleep(1)
        layout['task'].update(Panel(f'[bold green]{item}[/bold green] processed, {q.qsize()} tasks remaining in queue', title='Task'))
        q.task_done()

threading.Thread(target=worker, daemon=True).start()


console.log("Starting queue")
# Send thirty task requests to the worker.

with Live(layout, refresh_per_second=10, screen=True):
    for item in range(15):
        q.put(item)
        layout['pipe'].update(Panel(f'[bold green]{item}[/bold green] sent to queue'))
        if item and not item % 8:
            time.sleep(10)

    q.join()
