kingdom = []
count = 0

def add_knight(knight:str) -> None:
    global count
    kingdom.append(knight)
    print(id(kingdom))
    count += 1
    print(id(kingdom))

