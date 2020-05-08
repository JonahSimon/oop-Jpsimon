class Player:
    def __init__(self, faction : str = "None", role : str = "None"):
        self._faction : str = faction
        self._role : str = role

    @property
    def Faction(self) -> str:
        return self._faction

    def Role(self) -> str:
        return self._role

    def SetFaction(self, faction : str) -> None:
        self._faction = faction

    def SetRole(self, role : str) -> None:
        self._role = role
