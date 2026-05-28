import pylib.settings as settings
import logging

def add_knight(knight:str):
    global count

    kingdom.append(knight)
    count += 1

def add_knight_right_way(knight:str, kingdom:list, count:int):
    kingdom.append(knight)
    count += 1
    return count

if __name__ == '__main__':
    kingdom = []
    count = 0

    add_knight("Lancelot")
    logging.info(f"{kingdom == ["Lancelot"]=}")
    logging.info(f"{count == 1=}")

