
def add_knight(knight:str, kingdom:list=None):
    if kingdom is None:
        kingdom = []
    else:
        kingdom = kingdom.copy()

    kingdom.append(knight)

    return kingdom
