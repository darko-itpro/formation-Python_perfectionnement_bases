
def add_knight(knight:str, kingdom=None):

    kingdom = [] if kingdom is None else kingdom.copy()

    if knight in kingdom:
        raise ValueError(f'Duplicate knight {knight}')

    kingdom.append(knight)
    return kingdom
