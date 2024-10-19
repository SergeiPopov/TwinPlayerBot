from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, url: str, user: str):
        self.url = url
        self.user = user
        self.player_info = ""

    @abstractmethod
    def play(self):
        ...

    @abstractmethod
    def pause(self):
        ...

    @abstractmethod
    def resume(self):
        ...

    @abstractmethod
    def shuffle(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @abstractmethod
    def get_player_info(self):
        ...

    @abstractmethod
    def get_current_music_info(self):
        ...
