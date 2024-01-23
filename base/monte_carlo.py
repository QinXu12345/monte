from abc import ABC, abstractmethod
from typing import Callable,Any,Tuple
from scipy.stats.distributions import rv_continuous,rv_discrete
import numpy as np

Distribution = rv_continuous | rv_discrete

class MCBase(ABC):
    __slots__ = ['func','dist']
    
    def __init__(
        self,
        func: Callable[...,Any],
        dist: Distribution
    ):
        self.func = func
        self.dist = dist
        
    @abstractmethod
    def integrate(self):
        ...
        