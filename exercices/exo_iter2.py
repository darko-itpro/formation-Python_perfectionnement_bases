from collections import namedtuple
from pylib.datasources import pyflix

Episode = namedtuple("Episode", ['title', 'season', 'number', 'duration', 'year'])

pyflix.load_season()