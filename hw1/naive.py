from base.ball import Ball
from base.cube import Cube
from base.monte_carlo import Distribution, MCBase
from typing import Any, Iterable
from numpy.typing import NDArray
import numpy as np
from scipy.stats.distributions import uniform
from functools import partial

def radius_indicator(
    x: NDArray,
    radius: float | int
) -> NDArray:
    norm = np.sum(x**2,axis=1)
    mask = np.where(norm <= radius, 1, 0)
    return mask
        

class NaiveMC(MCBase):
    def __init__(
        self, 
        dim: int,
        center: Iterable[float] = (0,0),
        radius: int | float = 1.0,
        n_samples: int = 1000
        ):
        self._ball = Ball(dim,center,radius)
        self._cube = Cube(dim,center,length= 2*radius)
        loc = np.array(center) - radius
        scale = np.abs(loc) - loc
        u = uniform(loc=loc, scale=scale)
        fix_r = partial(radius_indicator,radius = radius)
        super().__init__(fix_r,u)
        self.n_samples = n_samples
        self._dim = dim
        
    def integrate(self):
        x = self.dist.rvs(size=(self.n_samples,self._dim))
        fx = self.func(x)
        inside = np.sum(fx, axis=0)
        return inside / self.n_samples,fx
    
    def estimate_volume(self):
        v_cube = self._cube.volume()
        return v_cube * self.integrate()[0]
    
    def estimate_area(self):
        return (self._dim + 1) * self.estimate_volume()
    
    def cube_volume(self):
        return self._cube.volume()
    
    def cube_area(self):
        return self._cube.area()
    
    def ball_volume(self):
        return self._ball.volume()
    
    def ball_area(self):
        return self._ball.area()
    
    def var(self):
        mean,fx = self.integrate()
        mse = np.sum((fx - mean)**2,axis=0) / (len(fx) - 1)
        return self.cube_volume()**2 * mse / len(fx)