import numpy as np

from error_propagation.core import Complex


class TestNumpyIntegration:
    def test_numpy_list_creation(self):
        np_list = np.array([Complex(1, 2), Complex(3, 4)])
        assert np_list is not None

    def test_numpy_list_addition(self):
        a = np.array([Complex(3, 4), Complex(8, 3)])
        b = np.array([Complex(2, 3), Complex(10, 4)])
        result = a + b

        expected_result = np.array([Complex(5, 5), Complex(18, 5)])

        assert all(result == expected_result)

    def test_pow(self):
        assert np.array([2, 3]) ** Complex(3, 3) is not None
        assert np.array([2, 3]) ** np.array([Complex(3, 3), Complex(3, 3)]) is not None
        assert (
            np.array([Complex(3, 3), Complex(3, 3)])
            ** np.array([Complex(3, 3), Complex(3, 3)])
            is not None
        )
        assert np.array([Complex(3, 3), Complex(3, 3)]) ** np.array([3, 3]) is not None
        assert np.array([Complex(3, 3), Complex(3, 3)]) ** 3 is not None

    def test_add(self):
        result = np.array([Complex(1, 2), Complex(4, 1)]) + 2
        expected_result = np.array([Complex(3, 2), Complex(6, 1)])
        assert (result == expected_result).all()
