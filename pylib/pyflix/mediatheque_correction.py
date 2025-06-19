class Episode:
    def __init__(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        self.title = title.title()
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
        try:
            return self._episodes.pop(0)
        except IndexError:
            raise StopIteration


class TvShow:
    def __init__(self, name):
        self.name = name
        self._episodes = []

    def __iter__(self):
        return EpisodesIterator(self.episodes)

    def __len__(self): # len(tvshow)
        return len(self._episodes)

    def __contains__(self, episode:Episode): # item in tvshow
        return episode in self._episodes

    def __getitem__(self, item): # tvshow[kekchose]
        pass

    @property
    def duration(self):
        return sum((episode.duration
                    for episode in self._episodes))

    @property
    def episodes(self):
        return self._episodes.copy()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title()

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
        return EpisodesIterator(self.episodes.copy())

    def add_episode(self, episode:Episode):
        self.episodes.append(episode)
