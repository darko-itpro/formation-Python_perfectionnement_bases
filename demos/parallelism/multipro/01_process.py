
import time
from rich.console import Console

console = Console()

def countdown(n):
    while n > 0:
        n -= 1


def main(value):

    console.rule("Sequential")

    console.log("Main    : before sequential")
    start_time = time.time()
    countdown(value)
    countdown(value)
    end_time = time.time()
    console.log(f"Main    : Collecting after {end_time - start_time:.4f} seconds")

    console.print()
    console.rule("Tasked")

    console.log("Main    : setting up")
    start_time = time.time()

    first_thread = Task(target=countdown, args=(value,))
    second_thread = Task(target=countdown, args=(value,))

    console.log("Main    : starting tasks")
    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    end_time = time.time()
    console.log(f"Main    : Collecting after {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    console.clear()

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-p", "--processed", action="store_true")
    parser.add_argument("-l", "--loops", type=int, default=100_000_000)

    args = parser.parse_args()

    if args.processed:
        from multiprocessing import Process as Task

        # freeze_support() est nécessaire avec rich
        from multiprocessing import freeze_support
        freeze_support()

        console.log("Using processes")
    else:
        from threading import Thread as Task
        console.log("Using threads")

    console.log(f"Loops: {args.loops}")
    main(args.loops)
