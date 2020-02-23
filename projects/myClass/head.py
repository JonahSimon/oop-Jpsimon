class Head:
    NUMBER_OF_HEADS : int = 1
    HIT_POINTS : int = 15
    CRIPPLED : bool = False

    def __init__(self, heads : int = NUMBER_OF_HEADS, hp : int = HIT_POINTS, crippled : bool = CRIPPLED):
        self._heads = heads
        self._crippled = crippled
        self._hitpoints = hp

    @property
    def NumHeads(self) -> int:
        return self._heads

    @property
    def crippled(self) -> bool:
        return self._crippled
    
    @property
    def HP(self) -> int:
        return self._hitpoints

    @HP.setter
    def hp(self,value : int) -> None:
        if value <=0:
            self._crippled = True
        if self._crippled: 
            self._hitpoints = 0
        else:
            self._health = value
