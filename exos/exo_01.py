
kingdom = []
count = 0

def add_knight(knight:str):
    global count

    kingdom.append(knight)
    count += 1

add_knight("Lancelot")
print(kingdom, count)

def add_knight_right_way(knight:str, kingdom:list, count:int):
    kingdom.append(knight)
    count += 1
    return count

count = add_knight_right_way("Robin", kingdom, count)
