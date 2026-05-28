
def add_knight(knight:str, kingdom:list=None):
    kingdom = [] if kingdom is None else kingdom.copy()
    if knight in kingdom:
        raise ValueError('knight already taken')

    kingdom.append(knight)
    return kingdom
