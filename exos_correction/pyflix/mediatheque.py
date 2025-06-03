class Episode:
    def __init__(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = int(duration) if duration is not None else None
        self.year = int(year) if year is not None else None

    def __str__(self):
        return f"{self.title} s{self.season_number}e{self.number}"

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
        try:
            return self._episodes.pop(0)
        except IndexError:
            raise StopIteration()


class TvShow:
    def __init__(self, name:str):
        self.name = name
        self._episodes = []

    def __len__(self):
        return len(self._episodes)

    def __contains__(self, item):
        return item in self._episodes


    def __iter__(self):
        return EpisodesIterator(self.episodes)


    @property
    def duration(self):
        return sum( episode.duration for episode in self._episodes )


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

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

    def add_episode(self, episode):
        self.episodes.append(episode)
