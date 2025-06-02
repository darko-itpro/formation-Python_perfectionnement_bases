
kingdom:list = []
count:int = 0

def add_knight(knight:str) -> None:
    global count
    kingdom.append(knight)
    count += 1

if __name__ == "__main__":
    add_knight('Lancelot')

    print(kingdom, count)
