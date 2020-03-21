class Character:
    def __init__(self, dead : bool = False):
        self._dead : bool = dead

    @property
    def Dead(self) -> bool:
        return self._dead

    def SetAlive(self) -> None:
        self._dead = False

    def SetDead(self) -> None:
        self._dead = True

    @property
    def Killed(self) -> bool:
        return self._dead