from typing import Iterable
from base.monte_carlo import MCBase
from base.ball import Ball
from base.cube import Cube
from scipy.stats import multivariate_normal
import numpy as np
from .naive import radius_indicator
from functools import partial


class ImportBallMC(MCBase):
    def __init__(
        self, 
        dim: int,
        center: Iterable[float] = (0,0),
        radius: int | float = 1.0,
        n_samples: int = 1000
        ):
        self._ball = Ball(dim,center,radius)
        self._cube = Cube(dim,center,length= 2*radius)
        loc = np.array(center)
        scale = radius * np.identity(dim)
        n = multivariate_normal(mean=loc,cov=scale)
        fix_r = partial(radius_indicator,radius = radius)
        super().__init__(fix_r,n)
        self.n_samples = n_samples
        self._dim = dim
        
    def integrate(self):
        x = self.dist.rvs(size=self.n_samples)
        fx = self.func(x)
        pdf = self.dist.pdf(x)
        inside = np.sum(fx / pdf, axis=0)
        return inside / self.n_samples,fx,pdf
    
    def estimate_volume(self):
        return self.integrate()[0]
    
    def estimate_area(self):
        return (self._dim + 1) * self.estimate_volume()
    
    def var(self):
        mean, fx, pdf = self.integrate()
        mse = np.sum((fx / pdf - mean) ** 2) / (len(fx) - 1)
        return mse / len(fx)
        