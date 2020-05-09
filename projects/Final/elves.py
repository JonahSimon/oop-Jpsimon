from player import Player

class Elf(Player):
    _role : str = "none"

    def __init__(self, elvishblessing : str = "none"):
        super(Elf,self).__init__(faction = "Elf")
        self._elvishblessing = elvishblessing

    @property
    def ElvishBlessing(self) -> str:
        return self._elvishblessing

    @ElvishBlessing.setter
    def SetElvishBlessing(self, blessing : str) -> None:
        self._elvishblessing = blessing