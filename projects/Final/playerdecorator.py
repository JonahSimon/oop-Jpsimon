from player import Player

class PlayerDecorator(Player):

    def __init__(self,decorated_player):
        self.decorated_player = decorated_player

    def Faction(self) -> str:
        return self.decorated_player.Faction

    def Role(self) -> str:
        return self.decorated_player.Role