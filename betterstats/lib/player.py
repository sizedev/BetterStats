from typing import List


class Player:
    def __init__(self, uid):
        self.uid = uid
        self.bases = None
        self.stats = None


class PlayerDB:
    def __init__(self, players: List[Player] = []):
        self.players = {p.uid: p for p in players}

    def get_player(self, uid: int) -> Player:
        return self.players[uid]

    def new_player(self, player: Player):
        if player.uid in self.players:
            raise ValueError(f"UID {player.uid} in use!")
        self.players[player.uid] = Player
