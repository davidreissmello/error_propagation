from math import log
from math import sqrt
import math

from error_propagation.core import Complex


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

    def test_right_addition(self):
        result = 1 + Complex(1, 3)
        assert result == Complex(2, 3)

    def test_subtraction(self):
        result = Complex(10, 3) - Complex(5, 4)
        assert result == Complex(5, 5)

    def test_right_subtraction(self):
        result = 1 - Complex(1, 3)
        assert result == Complex(0, 3)

    def test_multiplication(self):
        result = Complex(6, 7) * Complex(8, 9)
        assert result == Complex(6 * 8, sqrt(6 ** 2 * 9 ** 2 + 8 ** 2 * 7 ** 2))

    def test_right_multiplication(self):
        result = 1 * Complex(1, 1)
        assert result == Complex(1, 1)

    def test_division(self):
        result = Complex(8, 7) / Complex(4, 3)
        expected_error = sqrt((8 ** 2 * 3 ** 2) / (4 ** 4) + (7 ** 2) / (4 ** 2))
        assert result == Complex(2, expected_error)

    def test_right_division(self):
        result = 1 / Complex(1, 1)
        assert result == Complex(1, 1)

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

    def test_binary_operator(self):
        def value_f(x, y):
            return math.sin(x) + y

        def error_f(x, y):
            return 3 * x + 2 - y

        a = Complex(1, 3)
        b = Complex(3, 2)
        bin_op = Complex.binary_operator(value_f, error_f)

        result = bin_op(a, b)
        expected_result = Complex(value_f(a.value, b.value), error_f(a.error, b.error))
        assert result == expected_result

    def test_mono_operator(self):
        def value_f(x):
            return math.sin(x)

        def error_f(x):
            return math.cos(x) * 1.23 + 3

        a = Complex(1, 3)
        operator = Complex.mono_operator(value_f, error_f)

        result = operator(a)
        expected_result = Complex(value_f(a.value), error_f(a.error))
        assert result == expected_result
