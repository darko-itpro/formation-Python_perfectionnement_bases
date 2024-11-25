"""
Database management module
"""

import sqlite3 as sqlite
from collections import namedtuple
from pathlib import Path
import logging
from pylib import settings

SQL_CREATE_EPISODES_TABLE = "CREATE TABLE IF NOT EXISTS episodes ("\
                            "e_number INT NOT NULL, "\
                            "season INT NOT NULL, "\
                            "title TEXT NOT NULL, "\
                            "duration INT, "\
                            "year INT, "\
                            "PRIMARY KEY (e_number , season))"\
                            ";"
SQL_CREATE_SHOW_TABLE = "CREATE TABLE IF NOT EXISTS show ("\
                        "key TEXT NOT NULL, "\
                        "value TEXT NOT NULL, "\
                        "PRIMARY KEY (key))"\
                        ";"

SQL_ADD_SHOW_DATA = "INSERT INTO show values (?, ?);"
SQL_GET_SHOW_DATA = "SELECT value FROM show WHERE key = ?;"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?, ?, ?);"
SQL_GET_EPISODE = "SELECT title, season, e_number, duration, year FROM episodes where season = ? and e_number = ?;"
SQL_GET_ALL_EPISODES = "SELECT title, season, e_number, duration, year FROM episodes ORDER BY season, e_number;"
SQL_GET_EPISODES_FOR_SEASON = "SELECT title, season, e_number, duration, year FROM episodes where season = ? ORDER BY e_number;"
SQL_COUNT_EPISODES = "SELECT COUNT(*) FROM episodes;"

KEY_SHOW_NAME = "name"


# In this module, the namedtuple is used instead of the Episode class so we can still use the
# attribute syntax.
Episode = namedtuple("Episode",
                     ('title', 'season_number', 'number', 'duration', 'year'),
                     defaults=[None, None])


class TvShow:
    """
    TV Show DAO (Data Access Object) for one single show.
    """
    def __init__(self, name:str):
        self._name = name.title()

        import re
        self._db_name = Path(settings.ROOT_PATH, re.sub("[ .()]", "_", name)).with_suffix('.db')  # Voir regex
        self._connect = sqlite.connect(self._db_name)

        try:
            cur = self._connect.cursor()
            cur.execute(SQL_CREATE_EPISODES_TABLE)
            cur.execute(SQL_CREATE_SHOW_TABLE)
            cur.execute(SQL_ADD_SHOW_DATA, (KEY_SHOW_NAME, self._name))

        except sqlite.Error as e:
            # This error will occur only if the table already exists
            cur.execute(SQL_GET_SHOW_DATA, (KEY_SHOW_NAME,))
            self._name = cur.fetchone()[0]


    def __del__(self):
        try:
            self._connect.close()

        except sqlite.Error as e:
            logging.warn("Could not close database")
            logging.warn(e)

    def __str__(self):
        return 'Media DB Connector ({})'.format(self._db_name)

    @property
    def name(self):
        return self._name

    def add_episode(self, title: str, ep_number: int, season_number: int,
                    duration: int = None, year: int = None):
        """
        Adds an episode to the collection.

        :param title: episode title
        :param ep_number: episode number
        :param season_number: season number
        :param duration: duration in minutes of the episode. Optional.
        :param year: year of the episode. Optional.
        :raises ValueError: if the episode already exists
        """
        try:
            with self._connect:
                cur = self._connect.cursor()
                cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, title, duration, year))
        except sqlite.IntegrityError as ext:
            raise ValueError(f"Episode {title} s{season_number}e{ep_number} exists") from ext

    def get_episodes(self, season: int = None):
        """
        Get episodes for a season.

        :param season: season number for the episodes. Optional
        :return: the list of episodes for a given season if provided. An empty list if the season
        does not exist. All episodes if no season is provided.
        """
        cur = self._connect.cursor()
        if season:
            cur.execute(SQL_GET_EPISODES_FOR_SEASON, (int(season),))
        else:
            cur.execute(SQL_GET_ALL_EPISODES)

        return [Episode(*episode_data)
                for episode_data in cur.fetchall()]


    @property
    def episodes(self):
        return self.get_episodes()

    def __len__(self):
        cur = self._connect.cursor()
        cur.execute(SQL_COUNT_EPISODES)
        return cur.fetchone()[0]

    def __contains__(self, item: Episode|tuple[int, int]):
        cur = self._connect.cursor()

        if isinstance(item, Episode):
            season = item.season_number
            number = item.number
        else:
            season, number = item

        cur.execute(SQL_GET_EPISODE, (season, number))
        return True if cur.fetchone else False

    def __iter__(self):
        return EpisodesIterator(self._db_name)


class EpisodesIterator:
    """
    Iterator on episodes from a datasource.
    """
    def __init__(self, datasource):
        self._datasource = Path(datasource)
        if not self._datasource.exists():
            raise ValueError(f'File {datasource} does not exist')

        self._connect = sqlite.connect(self._datasource)
        cur = self._connect.cursor()
        cur.execute(SQL_GET_ALL_EPISODES)

        self._episodes = [Episode(*episode_data)
                for episode_data in cur.fetchall()]

        self._connect.close()


    def __iter__(self):
        return self

    def __next__(self):
        next_episode = self._episodes.pop(0)
        if next_episode:
            return next_episode
        else:
            raise StopIteration()



