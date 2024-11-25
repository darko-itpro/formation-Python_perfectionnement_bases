"""
Useful features for CLI usage
"""

def display_shows(shows:dict):
    """
    Displays in the terminal informations from a dict of shows

    The show must have a `name` and `epiosdes` attribute. Episode objects must have a `title`
    attribute.

    :param shows: dict of episodes
    """
    for show in shows.values():
        print("\n-----")
        display_show(show)

def display_show(show):
    """
    Displays a TV Show.

    The show must have a `name` and `epiosdes` attribute. Episode objects must have a `title`
    attribute.
    """
    print(show.name)
    for episode in show.episodes:
        print(f" - {episode.title}")
