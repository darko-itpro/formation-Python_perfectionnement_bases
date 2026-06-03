
def add_knight(knight:str, kingdom:list=None):
    kingdom = [] if kingdom is None else kingdom.copy()

    kingdom.append(knight)
    return kingdom
