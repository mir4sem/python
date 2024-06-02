![изображение](https://github.com/mir4sem/python/assets/70198995/7d6addd5-2457-4298-93f3-907653b05a87)

$f\overrightarrow{z},\overrightarrow{x},\overrightarrow{y} = \sum_{i+1}^{n} \left (z_{n+1-i}^{3} - y_{n+1-[i/2]}^{2}-81x_{[i/2]}\right) ^ 6 $
 
Примеры результатов вычислений:

f([0.24, -0.09],
[-0.87, -0.26],
[-0.97, 0.1]) ≈ 4.68e+11
f([0.23, 0.64],
[0.54, -0.48],
[-0.01, -0.4]) ≈ 3.99e-01
f([0.3, 0.92],
[0.44, 0.68],
[-0.21, -0.75]) ≈ 4.78e+07
f([-0.86, 0.63],
[0.02, 0.91],
[0.92, -0.99]) ≈ 3.72e+11
f([-0.21, 0.82],
[1.0, 0.94],
[0.97, -0.43]) ≈ 4.93e+11

```python
import math as m


def main(z, y, x):
    n = len(z)
    su = 0
    for i in range(n):
        su += (z[n - i - 1] ** 3 - y[n - 1 - m.floor(i / 2)] ** 2
               - 81 * x[m.floor(i / 2)]) ** 6
    return su

```

```python
from math import floor


def main(z, y, x):
    n = len(z)
    result = 0
    for i in range(1, n + 1):
        z_index = n - i
        y_index = n - floor((i - 1) / 2) - 1
        x_index = floor((i - 1) / 2)
        result += (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6
    return result

```

```python
from math import floor


def main(z, y, x):
    n = len(z)

    def compute(i):
        z_index = n - i
        y_index = n - floor((i - 1) / 2) - 1
        x_index = floor((i - 1) / 2)
        return (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6

    result = sum(map(compute, range(1, n + 1)))
    return result

```

```python
from math import floor


def main(z, y, x):
    n = len(z)

    def compute(i):
        z_index = n - i
        y_index = n - floor((i - 1) / 2) - 1
        x_index = floor((i - 1) / 2)
        return (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6

    result = sum(map(compute, range(1, n + 1)))
    return result

```

```python
from math import floor


def main(z, y, x):
    n = len(z)

    def generator():
        for i in range(1, n + 1):
            z_index = n - i
            y_index = n - floor((i - 1) / 2) - 1
            x_index = floor((i - 1) / 2)
            yield (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6

    result = sum(generator())
    return result

```

```python
from math import floor
from functools import reduce


def main(z, y, x):
    n = len(z)

    def compute(i):
        z_index = n - i
        y_index = n - floor((i - 1) / 2) - 1
        x_index = floor((i - 1) / 2)
        return (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6

    result = reduce(lambda acc, i: acc + compute(i), range(1, n + 1), 0)
    return result

```

```python
from math import floor


class FunctionIterator:
    def __init__(self, z, y, x):
        self.z = z
        self.y = y
        self.x = x
        self.n = len(z)
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        z_index = self.n - self.i
        y_index = self.n - floor((self.i - 1) / 2) - 1
        x_index = floor((self.i - 1) / 2)
        result = (self.z[z_index] ** 3 -
                  self.y[y_index] ** 2 - 81 * self.x[x_index]) ** 6
        self.i += 1
        return result


def main(z, y, x):
    iterator = FunctionIterator(z, y, x)
    result = sum(iterator)
    return result

```

```python
from math import floor


def sum_decorator(func):
    def wrapper(z, y, x):
        n = len(z)
        result = 0
        for i in range(1, n + 1):
            result += func(z, y, x, i, n)
        return result
    return wrapper


@sum_decorator
def compute(z, y, x, i, n):
    z_index = n - i
    y_index = n - floor((i - 1) / 2) - 1
    x_index = floor((i - 1) / 2)
    return (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6


def main(z, y, x):
    return compute(z, y, x)

```

## 4 способ
```python
from math import floor


def recursive_sum(z, y, x, i, n):
    if i > n:
        return 0
    z_index = n - i
    y_index = n - floor((i - 1) / 2) - 1
    x_index = floor((i - 1) / 2)
    current_value = (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6
    return current_value + recursive_sum(z, y, x, i + 1, n)


def main(z, y, x):
    n = len(z)
    return recursive_sum(z, y, x, 1, n)

```
