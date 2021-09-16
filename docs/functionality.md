# Error Propagation

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

#### Create your own error propagation functions
```python
import math
from error_propagation import Complex

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
```