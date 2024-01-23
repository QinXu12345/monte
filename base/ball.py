from .geometry import Shape
from typing import Iterable
from functools import cache
from scipy.special import gamma
import numpy as np

class Ball(Shape):
    __slots__ = ['_radius']
    
    def __init__(
        self,
        dim: int,
        center:Iterable[float],
        radius: int | float
    ):
        if dim <= 1:
            raise ValueError(f"""The minimum dimension is required
                             to be at least two, but got {dim}""")
            
        if radius <= 0:
            raise ValueError(f"""The radius of a ball 
                             must be positive, but got {radius}""")
        super().__init__(dim,center)
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @cache
    def area(self):
        half_dim = (self.dim + 1) / 2
        s1 = (2 * np.pi ** (half_dim) / 
              gamma(half_dim))
        sn = self._radius ** (self.dim) * s1
        return sn
        
    @cache
    def volume(self):
        half_dim = self.dim / 2
        v = (np.pi ** (half_dim) / 
            gamma(half_dim + 1) * 
            self._radius ** self.dim)
        return v