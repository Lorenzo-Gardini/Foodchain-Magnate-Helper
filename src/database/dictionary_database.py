from src.database.database import Database
from src.model import GameStatus, PlayerStatus


class DictionaryDatabase(Database):
    def save_player_status(self, username: str, player: PlayerStatus):
        pass

    def get_player_status(self, username: str) -> PlayerStatus:
        pass

    def save_game_status(self, game_status: GameStatus):
        pass

    def get_game_status(self, username: str) -> GameStatus:
        pass

    def __init__(self):
        self._users = dict()
