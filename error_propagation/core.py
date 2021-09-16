from math import log
from math import sqrt
from typing import List
from typing import Tuple
from typing import Union

import numpy as np


class Complex:
    """Object to store value and error.
    The error should be the standard deviation of the value."""

    def __init__(self, value: float, error: float):
        """

        Args:
            value: Value
            error: Standard deviation of value
        """
        self.value = value
        self.error = error

    def __str__(self) -> str:
        return f"{self.value} \u00B1 {self.error}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: "Complex") -> bool:
        return (self.value == other.value) and (self.error == other.error)

    def __add__(self, other: "Complex") -> "Complex":
        try:
            return self.add(self, other)
        except AttributeError:
            return self.add(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __radd__(self, other: "Complex") -> "Complex":
        try:
            return self.add(self, other)
        except AttributeError:
            return self.add(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __sub__(self, other: "Complex") -> "Complex":
        try:
            return self.sub(self, other)
        except AttributeError:
            return self.sub(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __rsub__(self, other: "Complex") -> "Complex":
        try:
            return self.sub(self, other)
        except AttributeError:
            return self.sub(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __mul__(self, other: "Complex") -> "Complex":
        try:
            return self.mul(self, other)
        except AttributeError:
            return self.mul(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __rmul__(self, other: "Complex") -> "Complex":
        try:
            return self.mul(self, other)
        except AttributeError:
            return self.mul(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __truediv__(self, other: Union["Complex", float]) -> "Complex":
        try:
            return self.truediv(self, other)
        except AttributeError:
            return self.truediv(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __rtruediv__(self, other: Union["Complex", float]) -> "Complex":
        try:
            return self.truediv(self, other)
        except AttributeError:
            return self.truediv(self, Complex(other, 0))
        except Exception as e:
            raise e

    def __pow__(
        self, power: Union["Complex", float, List[float]], modulo=None
    ) -> Union["Complex", List["Complex"]]:
        power = check_complex_instance(power)
        if isinstance(power, np.ndarray):
            results = []
            for p in power:
                results.append(Complex(*self.pow(p)))
            return np.array(results)

        return Complex(*self.pow(power))

    # def __rpow__(self, other):

    @staticmethod
    def add(self: "Complex", other: "Complex") -> "Complex":
        new_value = self.value + other.value
        new_error = sqrt(self.error ** 2 + other.error ** 2)
        return Complex(new_value, new_error)

    @staticmethod
    def sub(self: "Complex", other: "Complex") -> "Complex":
        new_value = self.value - other.value
        new_error = sqrt(self.error ** 2 + other.error ** 2)
        return Complex(new_value, new_error)

    @staticmethod
    def mul(self: "Complex", other: "Complex") -> "Complex":
        new_value = self.value * other.value
        new_error = sqrt(
            self.error ** 2 * other.value ** 2 + self.value ** 2 * other.error ** 2
        )
        return Complex(new_value, new_error)

    @staticmethod
    def truediv(self: "Complex", other: "Complex") -> "Complex":
        new_value = self.value / other.value
        new_error = sqrt(
            (self.value ** 2 * other.error ** 2) / (other.value ** 4)
            + (self.error ** 2) / (other.value ** 2)
        )
        return Complex(new_value, new_error)

    def pow(self, power: Union["Complex", float]) -> Tuple[float, float]:
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


def check_complex_instance(
    value: Union[Complex, float]
) -> Union[Complex, List[Complex]]:
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


def arrays_to_complex(values: List[float], errors: List[float]) -> np.ndarray:
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
