from player import Player

class ImmortalDecorator(Player):
    _Immortal : bool = True

    def Faction(self) -> str:
        return self._faction
    
    def Role(self) -> str:
        return self._role

    def Immortal(self) -> bool:
        return self._Immortal