class Episode:
    def __init__(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = int(duration) if duration is not None else None
        self.year = int(year) if year is not None else None

    def __eq__(self, other:"Episode"):
        if not isinstance(other, self.__class__):
            return False

        return (self.number, self.season_number) == (other.number, other.season_number)

    def __str__(self):
        return f"Episode '{self.title}', s{self.season_number}e{self.number}"

class TvShow:
    def __init__(self, name):
        self.name = name.title()
        self.episodes = []

    def add_episode(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self.episodes:
            raise ValueError(f'Duplicate episode "{new_episode.title}"')

        self.episodes.append(new_episode)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.episodes = []

    def add_episode(self, episode):
        self.episodes.append(episode)
