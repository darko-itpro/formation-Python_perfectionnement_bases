from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Message:
    sender:str
    target:str
    content:str

    rejected:bool=False

class Filter(ABC):

    def set_next(self, filter):
        self._next = filter

    @abstractmethod
    def process_message(self, message):
        pass


class ProfanityFilter(Filter):
    forbidden_words = ['Crotte', 'Zut', 'Flute']

    def process_message(self, message):
        pass


class BannedFilter(Filter):
    def process_message(self, message):
        if message.content.sender in banned_senders:
            message.statut_rejected = True
        else:
            pass

        return message

