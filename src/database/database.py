from abc import ABC, abstractmethod

from src.model import PlayerStatus, GameStatus


class Database(ABC):

    @abstractmethod
    def save_player_status(self, username: str, player: PlayerStatus):
        pass

    @abstractmethod
    def get_player_status(self, username: str) -> PlayerStatus:
        pass

    @abstractmethod
    def save_game_status(self, game_status: GameStatus):
        pass

    @abstractmethod
    def get_game_status(self, username: str) -> GameStatus:
        pass



