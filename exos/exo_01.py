camelot = []
count = 0

def add_knight(knight:str, kingdom:list) -> list:
    global count

    kingdom = kingdom.copy()
    kingdom.append(knight)
    count += 1
    return kingdom

