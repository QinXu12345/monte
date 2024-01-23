from typing import Iterable
from .geometry import Shape
from functools import cache

class Cube(Shape):
    __slots__ = ['_length']
    
    def __init__(self, 
                 dim: int, 
                 center: Iterable[float],
                 length: float
            ):
        super().__init__(dim, center)
        if length <= 0:
            raise ValueError(f"""The length of the cube
                             must be greater than zero,
                             but got {length}""")
        self._length = length
        
    @property
    def length(self):
        return self._length
    
    @cache
    def area(self):
        return 2 * self.dim * self._length ** (self.dim-1)
        
    @cache
    def volume(self):
        return self._length ** self.dim