from dataclasses import dataclass, field

@dataclass(frozen=True)
class Episode:
    title: str
    number: int
    season_number: int
    duration: int = None
