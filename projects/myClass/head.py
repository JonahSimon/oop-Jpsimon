class Head:
    NUMBER_OF_HEADS : int = 1
    HIT_POINTS : int = 15

    def __init__(self, heads : int = NUMBER_OF_HEADS, hp : int = HIT_POINTS):
        self._heads = heads
        self._crippled : bool = False
        self._hitpoints = hp

    @property
    def NumHeads(self) -> int:
        return self._heads

    @property
    def crippled(self) -> bool:
        return self._crippled
    
    @property
    def hp(self) -> int:
        return self._hitpoints

    @hp.setter
    def pressure(self,value : int) -> None:
        if value <= 0:
            self._crippled = True
        self._hitpoints = value
 