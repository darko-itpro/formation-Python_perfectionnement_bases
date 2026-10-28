
def add_knight(knight:str, kingdom:list=None):
    if kingdom is None:
        kingdom = []
    kingdom.append(knight)
    return kingdom
