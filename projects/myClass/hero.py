from character import Character
from head import Head

class Hero(Character):
    NUMBER_OF_ARMS : int = 2
    NUMBER_OF_LEGS : int = 2
    NUMBER_OF_HEADS : int = 1
    COLOR : str = "unknown"
    HIT_POINTS : int = 50

    def __init__(self, arms : int = NUMBER_OF_ARMS, legs : int = NUMBER_OF_LEGS, \
        heads : int = NUMBER_OF_HEADS, hp : int = HIT_POINTS, color : str = COLOR):
        super(Hero,self).__init__(dead = False)
        self._arms = arms
        self._legs = legs
        self._heads = heads
        self._health = hp
        self._power : str = "none"
        self._color : str = color

    @property
    def NumArms(self) -> int:
        return self._arms

    @property
    def NumLegs(self) -> int:
        return self._legs

    @property
    def NumHeads(self) -> int:
        return self._heads

    @property
    def HP(self) -> int:
        return self._health

    @property
    def Power(self) -> str:
        return self._power 

    @property
    def Killed(self):
        if self._power == "Immortal" or "Resurrection":
            return False
        else :
            self.SetDead()
            return True
        
    @Power.setter
    def SetPower(self, power : str) -> None:
        self._power = power

    @HP.setter
    def hp(self,value : int) -> None:
        if self.Dead == True:
            self._health = 0

        elif value <=0:
            if self.Killed:
                self.SetDead()
                self._health = 0
            else :
                self._health = 1000

        else:
            self._health = value