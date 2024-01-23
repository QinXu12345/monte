from abc import ABC, abstractmethod
from typing import Iterable

class Shape(ABC):
    __slots__ = ['_dim','_center']
    
    def __init__(
        self,
        dim: int,
        center: Iterable[float]
    ):
        self._dim = dim
        self._center = center
        
    @property
    def dim(self):
        return self._dim
    
    @property
    def center(self):
        return self._center
    
    @abstractmethod
    def area(self):
        ...
        
    @abstractmethod
    def volume(self):
        ...