from math import log
from math import sqrt

import pytest

from error_propagation.core import Complex


class TestComplexClass:
    def test_complex_class_creation(self):
        assert Complex(value=3, error=1.2) is not None

    def test_complex_value_error_output(self):
        """Check that inputs other than int or float return a value error"""
        with pytest.raises(ValueError):
            Complex(value="hello", error=3)

        with pytest.raises(ValueError):
            Complex(value=3, error="world")

        with pytest.raises(ValueError):
            Complex(value="hello", error="world")


class TestOperations:
    def test_equality(self):
        assert Complex(1, 2) == Complex(1, 2)
        assert Complex(1, 2) != Complex(1, 3)

    def test_complex_non_complex_mixture(self):
        result = Complex(10, 3) + 5
        assert result == Complex(15, 3)

    def test_addition(self):
        result = Complex(10, 3) + Complex(5, 4)
        assert result == Complex(15, 5)

    def test_subtraction(self):
        result = Complex(10, 3) - Complex(5, 4)
        assert result == Complex(5, 5)

    def test_multiplication(self):
        result = Complex(6, 7) * Complex(8, 9)
        assert result == Complex(6 * 8, sqrt(6 ** 2 * 9 ** 2 + 8 ** 2 * 7 ** 2))

    def test_division(self):
        result = Complex(8, 7) / Complex(4, 3)
        expected_error = sqrt((8 ** 2 * 3 ** 2) / (4 ** 4) + (7 ** 2) / (4 ** 2))
        assert result == Complex(2, expected_error)

    def test_power(self):
        a = 3
        a_error = 4
        b = 2
        b_error = 5

        result = Complex(a, a_error) ** Complex(b, b_error)
        expected_error = sqrt(
            a ** (2 * b) * b_error ** 2 * log(a) ** 2
            + (a ** (2 * b) * a_error ** 2 * b ** 2) / (a ** 2)
        )

        assert result == Complex(a ** b, expected_error)
