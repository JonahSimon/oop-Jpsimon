from player import Player

class Elf(Player):
    _role : str = "none"

    def __init__(self, elvishblessing : str = "none"):
        super(Elf,self).__init__(faction = "Elf")
        self._elvishblessing = elvishblessing

    @property
    def Elvishblessing(self) -> str:
        return self._elvishblessing

    @Elvishblessing.setter
    def role(self, blessing : str) -> None:
        self._elvishblessing = blessing