import time
from rich.console import Console

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish:str, duration:int):
    time.sleep(duration)

console = Console()


def main():
    console.rule("Sequential")

    console.log("Main    : before sequential")
    start_time = time.time()
    cooking(*pasta)
    cooking(*meat)
    end_time = time.time()
    console.log(f"Main    : Collecting after {end_time - start_time:.2f} seconds")

    console.print()
    console.rule("Tasked")

    console.log("Main    : setting up")
    start_time = time.time()

    pasta_cook = Task(target=cooking, args=pasta)
    meat_cook = Task(target=cooking, args=meat)

    console.log("Main    : cooking started")
    pasta_cook.start()
    meat_cook.start()

    pasta_cook.join()
    meat_cook.join()

    end_time = time.time()
    console.log(f"Main    : Collecting after {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    console.clear()
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-p", "--processed", action="store_true")

    args = parser.parse_args()

    if args.processed:
        from multiprocessing import Process as Task
        from multiprocessing import freeze_support
        freeze_support()
        console.log("Using processes")
    else:
        from threading import Thread as Task
        console.log("Using threads")

    main()
