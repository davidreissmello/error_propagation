from math import isclose

from error_propagation.complex import Complex
from error_propagation.finance.npv import npv


class TestFinancialFunctions:
    def test_npv_no_error_propagation(self):
        result = npv(cash=[10, 11, 12], discount_rate=0.05)

        assert isclose(result.value, 29.87, abs_tol=0.005)

    def test_npv_w_error_propagation(self):
        result = npv(
            cash=[Complex(10, 2), Complex(11, 3), Complex(12, 1)],
            discount_rate=Complex(0.05, 0.001),
        )

        assert isclose(result.value, 29.87, abs_tol=0.005)
