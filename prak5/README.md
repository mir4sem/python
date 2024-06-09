![image](https://github.com/mir4sem/python/assets/70198995/83df9f65-4493-4352-be8c-5f654f4d92fd)

```python
def f(y):
    n = len(y)
    result = 0
    for i in range(1, n + 1):
        result += (1 - y[n + 1 - i - 1]**3 - 16 * y[n + 1 - i - 1]**2)
    return result

# Примеры использования:
print(f([0.74, -0.93, -0.25, -0.37, 0.64, 0.01]))
print(f([0.93, 0.26, 0.71, -0.7, -0.29, -0.25]))
print(f([0.82, -0.86, -0.27, -1.0, -0.26, -0.53]))
print(f([0.89, -0.02, -0.74, 0.88, 0.8, 0.74]))
print(f([-0.52, 0.5, -0.97, 0.12, 0.62, 0.32]))
```

![image](https://github.com/mir4sem/python/assets/70198995/9de6edd4-dd6c-4e2b-99dc-e6ef77bc2b81)

```python
import math

def f(z, x, y):
    n = len(z)
    result = 0
    for i in range(n):
        result += (47 * z[n - 1 - math.floor(i / 3)]**3 + x[math.floor(i / 2)] + y[math.floor(i / 3)]**2) ** 2 / 73
    return round(result, 2)

# Примеры использования:
print(f([0.81, -0.97, -0.19, 0.37, 0.37], [0.81, -0.05, 0.31, -0.89, 0.76], [-0.22, 0.41, 0.7, 0.85, -0.78])) # 5.62e-01
print(f([-0.84, 0.31, 0.89, -0.67, -0.84], [-0.35, 0.34, 0.55, 0.6, -0.52], [-0.99, 0.85, 0.67, -0.29, -0.75])) # 3.46e+01
print(f([0.6, -0.25, -0.95, -0.59, 0.24], [-0.36, 0.19, 0.92, -0.65, 0.87], [-0.24, 0.58, 0.51, 0.91, -0.38])) # 2.12e+00
print(f([-0.31, 0.82, 0.09, -0.72, -0.52], [0.55, -0.04, 0.99, -0.68, -0.65], [0.91, -0.41, 0.03, -0.13, -0.53])) # 9.05e+00
print(f([0.07, -0.9, 0.2, 0.28, -0.55], [-0.09, 0.54, 0.43, -0.97, -0.64], [0.85, -0.69, -0.84, 0.37, -0.27])) # 2.11e+00
```

![image](https://github.com/mir4sem/python/assets/70198995/3432b0c9-f174-4cc6-9910-f34255caf04e)

```python
import math

def f(y, x, z):
    n = len(z)
    result = 0
    for i in range(n):
        result += 91 * (33 * x [n-1-math.floor(i/2)]**3 + 46 * y[n-1-i] + 49 * z[n-1-i]**2) ** 4
    resulttemp = 49 * result
    return round(resulttemp, 2)

# Примеры использования:
print(f([-0.58, -0.91, 0.17, 0.02], [-0.95, 0.86, 0.98, -0.41], [-0.63, 0.92, -0.78, 0.85])) # 1.83e+10
print(f([-0.2, -0.72, 0.58, 0.82], [-0.24, -0.91, -0.57, -0.48], [0.63, -0.06, 0.76, -0.64])) # 7.96e+10
print(f([0.38, -0.39, 0.59, 0.89], [0.32, 0.09, 0.87, 0.62], [0.12, -0.57, 0.42, -0.26])) # 6.11e+10
print(f([0.29, 0.51, 0.13, -0.83], [-0.48, -0.0, -0.1, -0.47], [-0.77, -0.02, 0.13, 0.71])) # 1.61e+10
print(f([0.43, -0.34, -0.76, 0.15], [-0.97, 0.46, 0.28, 0.23], [-0.9, -0.79, 0.49, 0.48])) # 6.05e+10
```

![image](https://github.com/mir4sem/python/assets/70198995/4a947f7b-ce72-42d6-a5f7-0574721d9554)

```python
import math

def f(y, x, z):
    n = len(z)
    result = 0
    for i in range(n):
        z_index = n - 1 - math.floor(i / 3)
        y_index = n - 1 - math.floor(i / 2)
        term = 38 * z[z_index]**2 - 7 * x[i]**3 - y[y_index]

        result += 98 * math.log2(term) ** 6

    resulttemp = 34 * result
    return round(resulttemp, 2)

# Примеры использования:
print(f([0.88, -0.28, -0.33, -0.69, -1.0, -0.71, 0.83, 0.28], [-0.43, -0.36, -0.51, -0.13, -0.17, -0.46, -0.14, 0.69], [0.49, 0.91, -0.59, -0.46, 0.3, -0.21, -0.7, -0.21])) # 5.93e+07
print(f([0.62, 0.31, -0.2, 0.0, 0.77, 0.41, 0.83, 0.92],[-0.39, -0.94, 0.66, -0.14, -0.7, 0.03, 0.8, 0.16],[0.54, 0.55, 0.4, 0.64, 0.51, -0.84, 0.73, 0.36])) # 1.36e+08
print(f([-0.7, 0.43, 0.86, -0.28, 0.4, 0.17, -0.91, 0.86],[-0.62, -0.62, 0.83, -0.45, -0.45, -0.93, 0.61, 0.85],[0.81, 0.1, -0.79, -0.94, 0.2, -0.84, -0.65, -0.36])) # 1.18e+08
print(f([0.88, 0.08, 0.15, 0.56, -0.56, 0.6, 0.33, -0.37],[0.55, 0.68, -0.97, -0.59, 0.82, -0.95, -0.18, -0.47],[0.87, -0.92, -0.06, -0.96, -0.49, 0.9, 0.57, 0.48])) # 1.47e+08
print(f([0.38, 0.28, 0.83, 0.17, 0.89, -0.5, 0.23, -0.88],[-0.06, -0.08, 0.22, -0.29, 0.79, -0.92, -0.61, -0.54],[-0.16, -0.34, 0.98, -0.03, 0.67, 0.91, 0.83, 0.47])) # 2.31e+08
```

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
