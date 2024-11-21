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

class EpisodesIterator:
    def __init__(self, episodes):
        self._episodes = episodes.copy()

    def __iter__(self):
        return self

    def __next__(self):
        if self._episodes:
            return self._episodes.pop(0)
        else:
            raise StopIteration('End of iteration')


class TvShow:
    def __init__(self, name:str):
        self.name = name.title()
        self._episodes = []

    @classmethod
    def wit_episodes(cls, name:str, episodes:list):
        pass

    @property
    def episodes(self):
        return self._episodes.copy()

    def __iter__(self):
        return EpisodesIterator(self.episodes)

    def add_episode(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self._episodes:
            raise ValueError(f'Duplicate episode "{new_episode.title}"')

        self._episodes.append(new_episode)

    def __getitem__(self, item):
        print(item, type(item))

class Playlist:
    def __init__(self, name):
        self.name = name
        self.episodes = []

    def __iter__(self):
        return EpisodesIterator(self.episodes)

    def add_episode(self, episode):
        self.episodes.append(episode)
