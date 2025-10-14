
def add_knight(knight:str):
    global count
    count += 1
    kingdom.append(knight)

if __name__ == '__main__':
    count = 0
    kingdom = []
    add_knight("Lancelot")
    print(count, kingdom)

