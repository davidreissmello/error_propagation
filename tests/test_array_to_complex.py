from numpy import array
from pandas import DataFrame

from error_propagation.src.arrays_to_complex import arrays_to_complex
from error_propagation.src.complex import Complex


class TestArrayMethods:
    def test_arrays_to_complex(self):
        values = array([1, 2])
        errors = array([3, 4])

        result = arrays_to_complex(values=values, errors=errors)

        expected_output = array([Complex(1, 3), Complex(2, 4)])

        assert all(result == expected_output)

    def test_pandas_series_integration(self):
        df = DataFrame({"values": [1, 2], "errors": [3, 4]})

        df["complex_numbers"] = arrays_to_complex(
            values=df["values"], errors=df["errors"]
        )

        expected_output = array([Complex(1, 3), Complex(2, 4)])

        assert all(df["complex_numbers"].values == expected_output)
