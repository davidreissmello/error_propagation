from math import log
from math import sqrt
from numbers import Number
from typing import Union

import numpy as np


class Complex:
    """Object to store value and error.
    The error should be the standard deviation of the value."""

    def __init__(self, value, error):
        """

        Args:
            value: Value
            error: Standard deviation of value
        """
        if not isinstance(value, Number):
            raise ValueError(f"Value {value} is not a number.")

        if not isinstance(error, Number):
            raise ValueError(f"Value {error} is not a number.")

        self.value = value
        self.error = error

    def __str__(self):
        return f"{self.value} \u00B1 {self.error}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.value == other.value) and (self.error == other.error)

    def __add__(self, other):
        other = check_complex_instance(other)
        new_value = self.value + other.value
        new_error = sqrt(self.error ** 2 + other.error ** 2)
        return Complex(value=new_value, error=new_error)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = check_complex_instance(other)
        new_value = self.value - other.value
        new_error = sqrt(self.error ** 2 + other.error ** 2)
        return Complex(value=new_value, error=new_error)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        other = check_complex_instance(other)
        new_value = self.value * other.value
        new_error = sqrt(
            self.error ** 2 * other.value ** 2 + self.value ** 2 * other.error ** 2
        )
        return Complex(value=new_value, error=new_error)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = check_complex_instance(other)
        new_value = self.value / other.value
        new_error = sqrt(
            (self.value ** 2 * other.error ** 2) / (other.value ** 4)
            + (self.error ** 2) / (other.value ** 2)
        )
        return Complex(value=new_value, error=new_error)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __pow__(self, power, modulo=None):
        power = check_complex_instance(power)
        if isinstance(power, np.ndarray):
            results = []
            for p in power:
                results.append(Complex(*self.pow(p)))
            return np.array(results)

        return Complex(*self.pow(power))

    # def __rpow__(self, other):

    def pow(self, power):
        new_value = self.value ** power.value
        new_error = (
            self.value ** (2 * power.value) * power.error ** 2 * log(self.value) ** 2
        )
        new_error += (
            self.value ** (2 * power.value)
            * (self.error ** 2 * power.value ** 2)
            / (self.value ** 2)
        )
        new_error = sqrt(new_error)
        return new_value, new_error


def check_complex_instance(value: Union[Complex, float]) -> Complex:
    """If value is not Complex, creates complex number with error 0.

    Args:
        value: complex number of value

    Returns:
        complex number

    """
    if isinstance(value, Complex):
        return value
    else:
        if isinstance(value, np.ndarray):
            complex_list = []
            for v in value:
                complex_list.append(Complex(v, 0))
            return np.array(complex_list)

        return Complex(value=value, error=0)


def arrays_to_complex(values: np.ndarray, errors: np.ndarray) -> np.ndarray:
    """Convert array of values and array of errors to array of Complex

    Args:
        values: array of values
        errors: array of errors

    Returns:
        array of complex values

    """
    return np.array(
        list(
            map(
                lambda value_error_tuple: Complex(
                    value_error_tuple[0], value_error_tuple[1]
                ),
                zip(values, errors),
            )
        )
    )
