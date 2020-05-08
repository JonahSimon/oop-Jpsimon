class Player:
    def __init__(self, faction : str = "None"):
        self._faction : str = faction

    @property
    def Faction(self) -> str:
        return self._faction

    @Faction.setter
    def SetFaction(self, faction : str) -> None:
        self._faction = faction