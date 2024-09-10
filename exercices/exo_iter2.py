from pprint import pprint

from collections import namedtuple
from pylib.datasources import pyflix

Episode = namedtuple("Episode", ['title', 'season', 'number', 'duration', 'year'])

episodes = []
for episode_data in pyflix.load_season():
    episodes.append(Episode(*episode_data[1:]))

print(episodes)

pprint([Episode(*episode_data[1:])
       for episode_data in pyflix.load_season()])