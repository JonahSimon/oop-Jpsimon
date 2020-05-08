from player import Player

class Orc(Player):
    _role : str = "none"

    def __init__(self, role : str = "none"):
        super(Orc,self).__init__(faction = "Orc")
        self._role = role

    @property
    def Role(self) -> str:
        return self._role

    @Role.setter
    def role(self, role : str) -> None:
        self._role = role