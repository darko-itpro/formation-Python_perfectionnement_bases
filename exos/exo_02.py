
def add_knight(knight:str, kingdom:list|None = None):
    kingdom = kingdom.copy() if kingdom is not None else []
    kingdom.append(knight)
    return kingdom
