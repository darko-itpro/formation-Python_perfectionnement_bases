import logging
import pylib.settings

logging.info("Script started")

kingdom:list[str] = []
count:int = 0

def add_knight(knight:str) -> None:
    global count
    kingdom.append(knight)
    count += 1

add_knight("Lancelot")
print(kingdom, count)


logging.info("script ended")