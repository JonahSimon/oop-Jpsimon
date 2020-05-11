from player import Player
from playerdecorator import PlayerDecorator

class ImmortalDecorator(PlayerDecorator):
    
    def __init__(self,decorated_player):
        PlayerDecorator.__init__(self,decorated_player)

    def Immortal(self) -> bool:
        return True
