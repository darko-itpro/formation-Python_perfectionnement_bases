
from threading import Thread
import time
from rich.console import Console


def countdown(n):
    while n > 0:
        n -= 1

value = 100_000_000

console = Console()
console.clear()

console.rule("Sequential")

console.log("Main    : before sequential")
start_time = time.time()
countdown(value)
countdown(value)
end_time = time.time()
console.log(f"Main    : Collecting after {end_time - start_time:.2f} seconds")


console.print()
console.rule("Threaded")

console.log("Main    : setting up")
start_time = time.time()

first_thread = Thread(target=countdown, args=(value,))
second_thread = Thread(target=countdown, args=(value,))

console.log("Main    : starting threads")
first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()

end_time = time.time()
console.log(f"Main    : Collecting after {end_time - start_time:.2f} seconds")
