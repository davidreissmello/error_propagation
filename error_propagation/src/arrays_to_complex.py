from numpy import array
from numpy import ndarray

from error_propagation.src.complex import Complex


def arrays_to_complex(values: ndarray, errors: ndarray) -> ndarray:
    """Convert array of values and array of errors to array of Complex

    Args:
        values: array of values
        errors: array of errors

    Returns:
        array of complex values

    """
    return array(
        list(
            map(
                lambda value_error_tuple: Complex(
                    value_error_tuple[0], value_error_tuple[1]
                ),
                zip(values, errors),
            )
        )
    )
