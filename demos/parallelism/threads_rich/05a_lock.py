import demos.parallelism.logger_conf
import logging
import threading
import time
from rich.console import Console


class Oven:
    def __init__(self):
        self._dish:str|None = None
        self._lock = threading.Lock()

    def cook_meal(self, dish:str, duration:int):
        console.log(f"Ready to cook {dish}")

        #with self._lock:
        #self._lock.acquire()
        console.log(f"➡️ Putting {dish} into oven ⏲️")
        self._dish = dish
        time.sleep(duration)
        console.log(f"⏏️ Taking out {self._dish} from oven ⏰")
        #self._lock.release()

console = Console()
console.clear()

console.rule("Starting…")

if __name__ == '__main__':
    pastry_01 = ("🥖 Bred", 8)
    pastry_02 = ("🧁 Cake", 4)

    oven = Oven()

    bread_cooker = threading.Thread(target=oven.cook_meal, args=pastry_01)
    cake_cooker = threading.Thread(target=oven.cook_meal, args=pastry_02)

    bread_cooker.start()
    cake_cooker.start()
