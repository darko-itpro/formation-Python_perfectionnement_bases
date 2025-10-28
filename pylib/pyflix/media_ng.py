"""
Module destiné à illustrer l'utilisation des dataclasses à la place des classes
*classiques*. Avec ses avantages et inconvénients.
"""

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Episode:
    title: str = field(compare=False)
    number: int
    season_number:int
    duration:int = field(default=None, compare=False)
    year:int = field(default=None, compare=False)


@dataclass(frozen=True)
class TvShow:
    name:str
    episodes:list = field(default_factory=list, init=False)

    def add_episode(self, title:str, season_number:int, number:int,
                    duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self.episodes:
            raise ValueError(f'Duplicate episode "{new_episode.title}"')

        self.episodes.append(new_episode)

@dataclass(frozen=True)
class Playlist:
    name:str
    episodes:list = field(default_factory=list, init=False)

    def add_episode(self, episode):
        self.episodes.append(episode)
