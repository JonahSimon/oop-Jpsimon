from typing import Sequence
from head import Head


class monster:
    NUMBER_OF_ARMS : int = 2
    NUMBER_OF_LEGS : int = 2
    NUMBER_OF_HEADS : int = 1
    HIT_POINTS : int = 50

    def __init__(self, arms : int = NUMBER_OF_ARMS, legs : int = NUMBER_OF_LEGS, \
        heads : int = NUMBER_OF_HEADS, hp : int = HIT_POINTS):
        self._arms = arms
        self._legs = legs
        self._heads = heads
        self._dead : bool = False

    

    