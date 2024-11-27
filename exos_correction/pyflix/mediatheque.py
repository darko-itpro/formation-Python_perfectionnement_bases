class Episode:
    def __init__(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = int(duration) if duration is not None else None
        self.year = int(year) if year is not None else None

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.number, self.season_number) == (other.number, other.season_number)

class EpisodeIterator:
    def __init__(self, episodes):
        self._episodes = episodes.copy()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self._episodes.pop(0)
        except IndexError:
            raise StopIteration()

class TvShow:
    def __init__(self, name:str):
        self.name = name.title()
        self._episodes = []

    @classmethod
    def with_episodes(cls, name:str, episodes:list):
        show = cls(name)
        for episode in episodes:
            show.add_episode(*episode)

        return show

    def __iter__(self):
        return EpisodeIterator(self.episodes)

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self._episodes:
            raise ValueError(f'Duplicate episode "{new_episode.title}"')

        self._episodes.append(new_episode)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.episodes = []

    def __iter__(self):
        return EpisodeIterator(self.episodes.copy())

    def add_episode(self, episode:Episode):
        self.episodes.append(episode)
