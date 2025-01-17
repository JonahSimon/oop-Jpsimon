from player import Player

class Orc(Player):
   
    def __init__(self, tusktype : str = "none"):
        super(Orc,self).__init__(faction = "Orc")
        self._tusktype = tusktype

    @property
    def TuskType(self) -> str:
        return self._tusktype

    @TuskType.setter
    def SetTuskType(self,tusktype : str) -> None:
        self._tusktype = tusktype