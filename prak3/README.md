![image](https://github.com/mir4sem/python/assets/70198995/105273c2-5b35-4c4a-99ec-6fd2815b5428)

## 1 способ
```python
def main(b, m, n, p):
    result = 0
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            for k in range(1, b + 1):
                a1 = ((1 - k ** 3) ** 6) / 8
                a2 = p + 64 * (7 + i ** 3 + 40 * j) ** 7
                result += (a1 + a2)
    return result

```

```python
def main(b, m, n, p):
    return f(b, m, n, p)


def f(b, m, n, p):
    result = 0
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            for k in range(1, b + 1):
                a1 = ((1 - k ** 3) ** 6) / 8
                a2 = p + 64 * (7 + i ** 3 + 40 * j) ** 7
                result += (a1 + a2)
    return result

```

```python
import numpy as np


def main(b, m, n, p):
    j = np.arange(1, n + 1)
    i = np.arange(1, m + 1)
    k = np.arange(1, b + 1)
    K, I, J = np.meshgrid(k, i, j, indexing='ij')
    a = ((1 - K ** 3) ** 6)
    c = 8 + p + 64 * (7 + I ** 3 + 40 * J) ** 7
    result = np.sum(a / c)
    return result

```

```python
def main(b, m, n, p):
    result = 0
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            inner_sum = 0
            for k in range(1, b + 1):
                a = ((1 - k ** 3) ** 6) / 8
                c = p + 64 * (7 + i ** 3 + 40 * j) ** 7
                inner_sum += (a + c)
            result += inner_sum
    return result

```

## 2 способ
```python
def main(b, m, n, p):
    return sum(((1 - k ** 3) ** 6)
               / 8 + p + 64 * (7 + i ** 3 + 40 * j) ** 7
               for j in range(1, n + 1)
               for i in range(1, m + 1)
               for k in range(1, b + 1))

```

```python
from itertools import product


def main(b, m, n, p):
    terms = product(range(1, b + 1),
                    range(1, m + 1), range(1, n + 1))
    return sum(((1 - k ** 3) ** 6) /
               8 + p + 64 * (7 + i ** 3 + 40 * j) ** 7
               for k, i, j in terms)

```

## 3 способ
```python
from functools import reduce
import itertools


def main(b, m, n, p):
    ranges = [range(1, dim + 1) for dim in [b, m, n]]
    product = itertools.product(*ranges)

    def add_terms(accum, values):
        k, i, j = values
        term = ((1 - k ** 3) ** 6) / 8 + p + 64 * (7 + i ** 3 + 40 * j) ** 7
        return accum + term
    return reduce(add_terms, product, 0)

```
