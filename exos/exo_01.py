camelot = []
count = 0

def add_knight(knight:str, kingdom) -> None:
    global count
    count = count + 1
    kingdom.append(knight)

print(id(count), id(kingdom))
add_knight("Arthur", camelot)
print(id(count), id(kingdom))
add_knight("Lancelot")
print(id(count), id(kingdom))
print(kingdom)
print(count)