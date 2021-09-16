from error_propagation import Complex
import pytest


class TestEdgeCases:
    def test_negative_error_converts_to_positive(self):
        assert Complex(1, -3).error == 3

    def test_string_as_input(self):
        with pytest.raises(ValueError):
            Complex(value="hello", error=3)

        with pytest.raises(ValueError):
            Complex(value=3, error="world")

        with pytest.raises(ValueError):
            Complex(value="hello", error="world")

        assert Complex(1, 1) is not None
