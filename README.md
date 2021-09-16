# Error Propagation

__Every number should have an error, even if it's 0.__

To do so, we have created a python package that makes it easy to propagate errors when performing calculations. 

    (10 ± 3) + (11 ± 4) != (21 ± 7) 

To calculate the error when adding 2 numbers, the L2 norm must be calculated
   
    (10 ± 3) + (11 ± 4) != (21 ± (3 ** 2 + 4 ** 2) ** 0.5) == (21 ± 5)

Calculating the error when multiplying, dividing, exponentiation is significantly harder, but 
still important! Please checkout [this notebook](./docs/derivations.ipynb) for derivations of 
error propagation formulas. 

## How to use
Create a Complex class instance: 

#### Basic Functionality
```python
from error_propagation import Complex
a = Complex(10, 3)
b = Complex(11, 4)

# Compute basic operations
a + b # 21.0 ± 5.0
a - b # -1.0 ± 5.0
a * b # 110.0 ± 51.85556864985669
a / b # 0.9090909090909091 ± 0.42855841859385696
a ** b # 100000000000.0 ± 978367874409.4901

# Compute basic equalities
a == b # False
a != b # True
a < b # True
a <= b # True
a > b # False
a >= b # False
```

#### Numpy and Pandas integration
```python
from error_propagation import Complex, arrays_to_complex
import numpy as np 
import pandas as pd

a = np.array([Complex(3, 4), Complex(8, 3)])
b = np.array([Complex(2, 3), Complex(10, 4)])
a + b # array([5.0 ± 5.0, 18.0 ± 5.0], dtype=object)
a * b # array([6.0 ± 12.041594578792296, 80.0 ± 43.86342439892262], dtype=object)

df = pd.DataFrame({"values": [1, 2], "errors": [3, 4]})
df["complex_numbers"] = arrays_to_complex(values=df["values"], errors=df["errors"])
```

#### Financial functions
```python
from error_propagation import Complex
from error_propagation.finance import npv
result = npv(
            cash=[Complex(10, 2), Complex(11, 3), Complex(12, 1)],
            discount_rate=Complex(0.05, 0.001),
        )

result # 29.867184969225782 ± 3.432196994041631
```

#### Leverage functions
```python
from error_propagation import Complex
a = Complex(10, 3)
b = Complex(11, 4)

Complex.add(a, b) # 21.0 ± 5.0
Complex.sub(a, b) # -1.0 ± 5.0
Complex.mul(a, b) # 110.0 ± 51.85556864985669
Complex.truediv(a, b) # 0.9090909090909091 ± 0.42855841859385696
Complex.pow(a, b) # 100000000000.0 ± 978367874409.4901
```


To see more examples, go to [docs/functionality.md](./docs/functionality.md) and the [tests](./tests)folder. 

## How to install
error-propagation is hosted on [PyPi](https://pypi.org/project/error-propagation)
```ssh
pip install error-propagation
```