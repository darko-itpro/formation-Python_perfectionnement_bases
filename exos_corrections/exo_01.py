kingdom = []
count = 0

def add_knight(knight:str) -> None:
    global count
    kingdom.append(knight)
    count = count + 1

add_knight("Lancelot")
add_knight("Robin")

print(kingdom)
print(count)
