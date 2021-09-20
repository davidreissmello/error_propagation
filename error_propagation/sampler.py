from functools import partial
from typing import Callable, List, Any

import numpy as np
import numpy.random as rnd


class Sampler:
    """Object that propagates error by storing the random building blocks and implements
    the '.sample()' method
    """

    IMPLEMENTED_DISTRIBUTIONS = {
        "constant": lambda N, val: val * np.ones(N),
        "uniform": rnd.uniform,
        "normal": rnd.normal,
        "choice": rnd.choice,
        "bernoulli": partial(rnd.choice, [True, False]),
        "binomial": rnd.binomial,
        "geometric": rnd.geometric,
        "exponential": rnd.exponential,
        "poisson": rnd.poisson,
        "chisquare": rnd.chisquare,
        "gamma": rnd.gamma,
        "beta": rnd.beta,
        "triangular": rnd.triangular,
        "power": rnd.power,
        "composite": None,
    }

    def __init__(self, distribution: str, sample_fcn: Callable = None, *args, **kwargs):
        if distribution not in Sampler.IMPLEMENTED_DISTRIBUTIONS:
            raise ValueError(
                f"Distribution {distribution} is not defined. Try one of ['"
                + "', '".join(Sampler.IMPLEMENTED_DISTRIBUTIONS)
                + "']"
            )

        self.__distribution = distribution

        if distribution == "composite":
            self.__sample_fcn = sample_fcn
            return

        self.__sample_fcn = partial(
            Sampler.IMPLEMENTED_DISTRIBUTIONS[distribution], *args, **kwargs
        )

    def sample(self, size: int) -> np.array:
        """Extracts N samples from random variable

        Args:
            N (int): Number of samples

        Returns:
            np.array: Array length N of samples from distribution
        """
        return self.__sample_fcn(size=size)

    def mean(self, size: int = 10000) -> float:
        """Simulates the mean of the distribution

        Args:
            size (int): Number of elements used in calculation

        Returns:
            float: simulated mean
        """
        if hasattr(self, "_Sampler__N_mean"):
            if self.__N_mean >= size:
                return self.__mean

        self.__N_mean = size
        self.__mean = np.mean(self.sample(size))
        return self.__mean

    def std(self, size: int = 10000) -> float:
        """Simulates the standard deviation of the distribution

        Args:
            size (int): Number of elements used in calculation

        Returns:
            float: simulated standard deviation
        """
        if not hasattr(self, "__N_std") or (self.__N_std < size):
            self.__N_std = size
            self.__std = np.std(self.sample(size))

        return self.__std

    def var(self, size: int = 10000) -> float:
        """Simulates the variance of the distribution.

        Args:
            size (int): Number of elements used in calculation

        Returns:
            float: simulated variance
        """
        if not hasattr(self, "__N_var") or (self.__N_var < size):
            self.__N_var = size
            self.__var = np.var(self.sample(size))

        return self.__var

    def __str__(self):
        return f"{self.__distribution}: {self.mean()} \u00B1 {self.std()}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Sampler("constant", val=other)

        def sample_fcn(size):
            X_samples = self.sample(size)
            Y_samples = other.sample(size)
            return X_samples + Y_samples

        return Sampler("composite", sample_fcn)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Sampler("constant", val=other)

        def sample_fcn(size):
            X_samples = self.sample(size)
            Y_samples = other.sample(size)
            return X_samples - Y_samples

        return Sampler("composite", sample_fcn)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Sampler("constant", val=other)

        def sample_fcn(size):
            X_samples = self.sample(size)
            Y_samples = other.sample(size)
            return X_samples * Y_samples

        return Sampler("composite", sample_fcn)

    def __true_div__(self, other):
        if isinstance(other, (int, float)):
            other = Sampler("constant", val=other)

        def sample_fcn(size):
            X_samples = self.sample(size)
            Y_samples = other.sample(size)
            return X_samples / Y_samples

        return Sampler("composite", sample_fcn)

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            other = Sampler("constant", val=other)

        def sample_fcn(size):
            X_samples = self.sample(size)
            Y_samples = other.sample(size)
            return X_samples ** Y_samples

        return Sampler("composite", sample_fcn)
