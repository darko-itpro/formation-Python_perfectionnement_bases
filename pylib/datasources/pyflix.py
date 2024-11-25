"""
This module is a datasource for different cases studied.
"""

from pathlib import Path
import random
random.seed()

def load_season(show_name=None, season_number=None):
    file_path = Path(__file__).resolve().parent.parent.parent / "assets" / "bbts12.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        episodes = [_process_line(line) for line in bbt_file]

    return episodes


def get_season(user=None) -> list:
    """
    Function to get a season of a Tv Show. Without any parameter (so, with `None`), returns a list
    of titles of the episodes of the season. With a parameter, returns the list as a dict.

    The number of viewed/not viewed episodes is random. Each episode has 80% chances to be viewed.
    Once an episode is viewed, all the following episodes are viewed. A non-viewed episode have
    60% chances to be without the kew `viewed`.

    :param user: a user ID (any value but `None`).
    :return: If an id is provided, a list of episodes where each episode is a dict with the keys
    `title`, `duration` and `viewed`. if the episode was not viewed, the `viewed` key may be
    missing.
    """
    file_path = Path(__file__).resolve().parent.parent.parent / "assets" / "bbts12.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        episodes = [_to_dict(*_process_line(line)) for line in bbt_file]

        if user is not None:
            _randomize_viewed(episodes)

    return episodes


def _randomize_viewed(season: list) -> None:
    """
    Randomly adds a key `viewed` to a list of episodes.

    An episode has 80% chances to be `viewed`. Once an episode is set to `not viewed`, all the
    following are also not viewed. `Not viewed` episodes have 60% chances to have the key missing.

    :param season: A list of dicts.
    """
    is_viewed = True


    for episode in season:
        if random.random() > 0.8:
            is_viewed = False

        if is_viewed:
            episode['viewed'] = True
        else:
            if random.random() > 0.6:
                episode['viewed'] = False

def _process_line(episode_line: str):
    """
    Reads and

    :param episode_line: A line from a csv file
    :return: A tuple (season name, season number, episode number, episode title, duration, year).
    """
    show, season, episode, title, duration, year = episode_line.rstrip().split(';')
    return show, title, int(season), int(episode), int(duration), int(year)


def _to_dict(show, title, season, episode, duration, year):
    episode = {"title": title, "duration": duration}
    return episode
