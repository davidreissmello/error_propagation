from numbers import Number
from typing import List
from typing import Union

import numpy as np

from error_propagation.src.complex import Complex


def npv(
    cash: Union[List[Number], List[Complex]],
    discount_rate: Union[Number, Complex],  # noqa
) -> Complex:
    """NPV accounts for the time value of money and can be used to compare
    similar investment alternatives. The NPV relies on a discount rate that
    may be derived from the cost of the capital required to invest, and any
    project or investment with a negative NPV should be avoided. One
    important drawback of NPV analysis is that it makes assumptions about
    future events that may not be reliable.

    For more information on NPV, see below
    https://www.investopedia.com/terms/n/npv.asp

    Args:
        cash: Net cash inflow-outflows during a single period t
        discount_rate: Discount rate or return that could be earned in
    alternative investments

    Returns:
        present value of an investment's future cash flows above the
        investment's initial cost



    """
    denominator = (Complex(1, 0) + discount_rate) ** np.arange(1, len(cash) + 1)
    cash = list(map(lambda x: x if isinstance(x, Complex) else Complex(x, 0), cash))
    return np.sum(np.array(cash) / denominator)
