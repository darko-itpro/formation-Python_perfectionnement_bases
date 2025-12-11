import demos.parallelism.logger_conf
import logging
import threading
import time
import random

from dataclasses import dataclass, field

from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()

menu = [
    ("Burger with fries", 8),
    ("Hot Dog", 5),
    ("Pizza Napolitana", 4),
    ("Fish and chips", 7),
    ("Venison Stew", 10),
]


@dataclass
class Order:
    name: str
    duration: int
    status: str = field(default="Ordered", init=False)

    @property
    def remaining_time(self):
        try:
            r_time =  self.duration - (time.time() - self._start_time)
        except AttributeError:
            r_time = self.duration

        if r_time < 0:
            r_time = 0
        return round(r_time)

    def start_cooking(self):
        self._start_time = time.time()
        self.status = "Cooking"

    def done(self):
        self.status = "Done"

    def is_done(self):
        return self.status == "Done"


def make_table(order_list:list[Order]) -> Table:
    table = Table(
        title="Service du Soir",
    )

    table.add_column("Order", width=30)
    table.add_column("Ready in")
    table.add_column("Status")

    for order in order_list:

        if order.status == "Ordered":
            status_str = f"{order.status:^13}"
        elif order.status == "Cooking":
            status_str = f"[white on red]{order.status:^13}[/]"
        elif order.status == "Done":
            status_str = f"[white on dark_green]{order.status:^13}[/]"
        else:
            status_str = "[red]ERROR[/]"

        table.add_row(order.name, f"{order.remaining_time}", status_str)

    if len(order_list) < 10:
        for _ in range(10 - len(order_list)):
            table.add_row("", "", "")

    return table


class KitchenTeam:
    def __init__(self, team=4):
        self._team = threading.Semaphore(value=team)

    def cook(self, order:Order):
        with self._team:
            order.start_cooking()
            time.sleep(order.duration)
            order.done()


kitchen = KitchenTeam(4)

available_orders = random.randint(30, 50)
threshold = 40

orders_list = []


def still_serving(orders_list:list[Order]):
    if not orders_list:
        return True
    return not all(order.is_done() for order in orders_list)


console.clear()

with Live(make_table(orders_list), console=console) as live:
    while available_orders or still_serving(orders_list):
        if available_orders and random.randint(0, 100) < threshold:
            new_client_order = Order(*random.choice(menu))
            orders_list.append(new_client_order)
            in_process = threading.Thread(target=kitchen.cook, args=(new_client_order,))
            in_process.start()


            available_orders -= 1

        if len(orders_list) > 10:
            orders_list = orders_list[-10:]

        if threshold < 60:
            threshold += 1

        live.update(make_table(orders_list))

        time.sleep(1)
    live.update(make_table(orders_list))
