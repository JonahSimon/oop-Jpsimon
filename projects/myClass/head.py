class Head:
    NUMBER_OF_HEADS : int = 1
    HIT_POINTS : int = 50

    def __init__(self, heads : int = NUMBER_OF_HEADS, hp : int = HIT_POINTS):
        self._heads = heads
        self._crippled : bool = False
        self._hitpoints = hp
 