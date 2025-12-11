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

class DuplicateEpisodeError(ValueError):
    pass

class TvShow:
    def __init__(self, name):
        self.name = name.title()
        self._episodes = []

    @property
    def duration(self):
        return sum((episode.duration
                    for episode in self._episodes))

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title:str, season_number:int, number:int,
                    duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self._episodes:
            raise DuplicateEpisodeError(f'Duplicate episode "{new_episode.title}"')

        self._episodes.append(new_episode)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.episodes = []

    def add_episode(self, episode):
        self.episodes.append(episode)
