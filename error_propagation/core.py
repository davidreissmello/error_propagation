from math import log, sqrt
from typing import List
from typing import Union, Callable
from numbers import Number
import operator
import numpy as np
from functools import wraps


def _try_except_wrapper(self: "Complex", other: "Complex", func: Callable):
    try:
        return func(self, other)
    except AttributeError:
        return func(self, Complex(other, 0))
    except Exception as e:
        raise e


def _try_except_wrapper_comparison(self: "Complex", other: "Complex", func: Callable):
    try:
        return func(self.value, other.value)
    except AttributeError:
        return func(self.value, other)
    except Exception as e:
        raise e


def ndarray_safe(func):
    @wraps(func)
    def ndarray_safe_wrapper(complex, target, *args, **kwargs):
        if isinstance(target, np.ndarray):
            complexlist = [func(complex, item, *args, **kwargs) for item in target]
            return np.asarray(complexlist)
        return func(complex, target, *args, **kwargs)

    return ndarray_safe_wrapper


class Complex:
    """Object to store value and error.
    The error should be the standard deviation of the value."""

    def __init__(self, value: float, error: float):
        """

        Args:
            value: Value
            error: Standard deviation of value
        """
        if not isinstance(value, Number):
            raise ValueError(f"Value {value} is not a float")
        if not isinstance(error, Number):
            raise ValueError(f"Error {value} is not a float")

        self.value = float(value)
        self.error = abs(float(error))

    def __str__(self) -> str:
        return f"{self.value} \u00B1 {self.error}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: "Complex") -> bool:
        return (self.value == other.value) and (self.error == other.error)

    def __ne__(self, other: "Complex") -> bool:
        return (self.value != other.value) or (self.error != other.error)

    def __lt__(self, other: "Complex") -> bool:
        return _try_except_wrapper_comparison(self, other, operator.lt)

    def __le__(self, other: "Complex") -> bool:
        return _try_except_wrapper_comparison(self, other, operator.le)

    def __gt__(self, other: "Complex") -> bool:
        return _try_except_wrapper_comparison(self, other, operator.gt)

    def __ge__(self, other: "Complex") -> bool:
        return _try_except_wrapper_comparison(self, other, operator.ge)

    def __hash__(self) -> int:
        return hash((self.value, self.error))

    def __bool__(self) -> bool:
        return True

    @ndarray_safe
    def __add__(self, other: "Complex") -> "Complex":
        return _try_except_wrapper(self, other, Complex.add)

    def __radd__(self, other: "Complex") -> "Complex":
        return self.__add__(other)

    def __iadd__(self, other: "Complex") -> "Complex":
        return self.__add__(other)

    @ndarray_safe
    def __sub__(self, other: "Complex") -> "Complex":
        return _try_except_wrapper(self, other, Complex.sub)

    def __rsub__(self, other: "Complex") -> "Complex":
        return self.__sub__(other)

    def __isub__(self, other: "Complex") -> "Complex":
        return self.__sub__(other)

    @ndarray_safe
    def __mul__(self, other: "Complex") -> "Complex":
        return _try_except_wrapper(self, other, Complex.mul)

    def __rmul__(self, other: "Complex") -> "Complex":
        return self.__mul__(other)

    def __imul__(self, other: "Complex") -> "Complex":
        return self.__mul__(other)

    @ndarray_safe
    def __truediv__(self, other: Union["Complex", float]) -> "Complex":
        return _try_except_wrapper(self, other, Complex.truediv)

    def __rtruediv__(self, other: Union["Complex", float]) -> "Complex":
        return self.__truediv__(other)

    def __itruediv__(self, other: Union["Complex", float]) -> "Complex":
        return self.__truediv__(other)

    @ndarray_safe
    def __pow__(
        self, power: Union["Complex", List[float]]
    ) -> Union["Complex", List["Complex"]]:
        return _try_except_wrapper(self, power, Complex.pow)

    @ndarray_safe
    def __ipow__(self, other: "Complex") -> "Complex":
        return _try_except_wrapper(self, other, Complex.pow)

    def __rpow__(self, other):
        try:
            return self.pow(self, other)
        except AttributeError:
            # same as _try_except_wrapper but inverted
            return self.pow(Complex(other, 0), self)
        except Exception as e:
            raise e

    def __neg__(self) -> "Complex":
        return Complex(-self.value, self.error)

    def __pos__(self) -> "Complex":
        return self

    def __abs__(self) -> "Complex":
        return Complex(operator.abs(self.value), self.error)

    @staticmethod
    def add(a: "Complex", b: "Complex") -> "Complex":
        new_value = a.value + b.value
        new_error = sqrt(a.error ** 2 + b.error ** 2)
        return Complex(new_value, new_error)

    @staticmethod
    def sub(a: "Complex", b: "Complex") -> "Complex":
        new_value = a.value - b.value
        new_error = sqrt(a.error ** 2 + b.error ** 2)
        return Complex(new_value, new_error)

    @staticmethod
    def mul(a: "Complex", b: "Complex") -> "Complex":
        new_value = a.value * b.value
        new_error = sqrt(a.error ** 2 * b.value ** 2 + a.value ** 2 * b.error ** 2)
        return Complex(new_value, new_error)

    @staticmethod
    def truediv(a: "Complex", b: "Complex") -> "Complex":
        new_value = a.value / b.value
        new_error = sqrt(
            (a.value ** 2 * b.error ** 2) / (b.value ** 4)
            + (a.error ** 2) / (b.value ** 2)
        )
        return Complex(new_value, new_error)

    @staticmethod
    def mono_operator(
        value_fn: Callable[[float], float], error_fn: Callable[[float], float]
    ) -> Callable[["Complex"], "Complex"]:
        def call(a: "Complex") -> "Complex":
            new_value = value_fn(a.value)
            new_error = error_fn(a.error)
            return Complex(new_value, new_error)

        return call

    @staticmethod
    def binary_operator(
        value_fn: Callable[[float, float], float],
        error_fn: Callable[[float, float], float],
    ) -> Callable[["Complex", "Complex"], "Complex"]:
        def call(a: "Complex", b: "Complex") -> "Complex":
            new_value = value_fn(a.value, b.value)
            new_error = error_fn(a.error, b.error)
            return Complex(new_value, new_error)

        return call

    @staticmethod
    def pow(a, power: Union["Complex", float]) -> "Complex":
        new_value = a.value ** power.value
        new_error = a.value ** (2 * power.value) * power.error ** 2 * log(a.value) ** 2
        new_error += (
            a.value ** (2 * power.value)
            * (a.error ** 2 * power.value ** 2)
            / (a.value ** 2)
        )
        new_error = sqrt(new_error)
        return Complex(new_value, new_error)


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
