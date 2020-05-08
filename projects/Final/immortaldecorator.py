from player import Player
from playerdecorator import PlayerDecorator

class ImmortalDecorator(PlayerDecorator):
    def __init__(self):
        super(ImmortalDecorator,self)
        self._immortal : bool = True
