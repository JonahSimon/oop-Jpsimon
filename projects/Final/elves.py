from player import Player

class Elf(Player):
    _role : str = "none"

    def __init__(self, role : str = "none"):
        super(Elf,self).__init__(faction = "Elf")
        self._role = role

    @property
    def Role(self) -> str:
        return self._role

    @Role.setter
    def role(self, role : str) -> None:
        self._role = role