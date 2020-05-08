class Player:
    def __init__(self, faction : str = "None",  role : str = "none"):
        self._faction : str = faction
        self._role : str = role

    @property
    def Faction(self) -> str:
        return self._faction

    @Faction.setter
    def SetFaction(self, faction : str) -> None:
        self._faction = faction
    
    @property
    def Role(self) -> str:
        return self._role

    @Role.setter
    def role(self, role : str) -> None:
        self._role = role