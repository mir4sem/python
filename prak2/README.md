![изображение](https://github.com/mir4sem/python/assets/70198995/b440e45c-1fa7-4002-80d9-809642b875ee)

## 1 способ
```python
import math


def main(y):
    if y < 70:
        return ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
    elif 70 <= y < 158:
        return 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y
    elif 158 <= y < 251:
        return 0.08-72 * abs(y**3)-33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5
    elif 251 <= y < 320:
        return y**4 + 70 * math.pow(y, 7)
    return 5 * (y - (y**2/4))**4 + 1

```

```python
import math


def main(y):
    if y < 70:
        return ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
    elif 70 <= y < 158:
        return 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y
    elif 158 <= y < 251:
        a = 0.08 - 72 * abs(y**3) - 33
        return 0.08-72 * abs(y**3)-33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5
    elif 251 <= y < 320:
        return y**4 + 70 * math.pow(y, 7)
    else:
        return 5 * (y - (y**2/4))**4 + 1

```

```python
import math


def main(y):
    if y < 70:
        return func1(y)
    elif 70 <= y < 158:
        return func2(y)
    elif 158 <= y < 251:
        return func3(y)
    elif 251 <= y < 320:
        return func4(y)
    else:
        return func5(y)


def func1(y):
    return ((y ** 3 / 37) + 1) / 3 - 44 * (73 * y ** 3 - 1) ** 6


def func2(y):
    return 1 + (5 * y ** 2 - y - y ** 3) ** 3 + 60 * y


def func3(y):
    return 0.08 - 72 * abs(y ** 3) -
    (33 * math.tan(y ** 3 / 91 + 41 * y ** 2 + 76) ** 5)


def func4(y):
    return y ** 4 + 70 * y ** 7


def func5(y):
    return 5 * (y - (y ** 2 / 4)) ** 4 + 1

```

```python
import math


def main(y):
    if y < 70:
        a = ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
        return a
    elif 70 <= y < 158:
        a = 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y
        return a
    elif 158 <= y < 251:
        a = 0.08 - 72 * abs(y**3) - 33
        return 0.08-72 * abs(y**3)-33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5
    elif 251 <= y < 320:
        a = y**4 + 70 * math.pow(y, 7)
        return a
    a = 5 * (y - (y**2/4))**4 + 1
    return a

```

```python
from math import pow, tan


def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


def main(y):
    if y < 70:
        a = ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
        return a
    elif 70 <= y < 158:
        a = 1 + pow(5 * y**2 - y - y**3, 3) + 60 * y
        return a
    elif 158 <= y < 251:
        a = 0.08 - 72 * my_abs(y**3) - 33
        b = tan(y**3 / 91 + 41 * y**2 + 76)**5
        return 0.08-72 * my_abs(y**3)-33 * tan(y**3 / 91 + 41 * y**2 + 76)**5
    elif 251 <= y < 320:
        a = y**4 + 70 * pow(y, 7)
        return a
    return 5 * (y - (y**2/4))**4 + 1

```

```python
import math


def main(y):
    if y < 70:
        a = ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
    elif 70 <= y < 158:
        a = 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y
    elif 158 <= y < 251:
        c = 0.08 - 72 * abs(y**3) - 33
        b = math.tan(y**3 / 91 + 41 * y**2 + 76)**5
        a = c * b
    elif 251 <= y < 320:
        a = y**4 + 70 * math.pow(y, 7)
    else:
        a = 5 * (y - (y**2/4))**4 + 1
    return a

```

```python
import math


def main(y):
    if y < 70:
        a = ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
    elif 70 <= y < 158:
        a = 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y
    elif 158 <= y < 251:
        a = 0.08-72 * abs(y**3)-33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5
    elif 251 <= y < 320:
        a = y**4 + 70 * math.pow(y, 7)
    else:
        a = 5 * (y - (y**2/4))**4 + 1
    return a

```

```python
import math


def main(y):
    if y < 70:
        a = ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
    elif y < 158:
        b = (5 * y**2 - y - y**3, 3)
        a = 1 + math.pow(b, 3) + 60 * y
    elif y < 251:
        a = 0.08-72 * abs(y**3)-33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5
    elif y < 320:
        a = y**4 + 70 * math.pow(y, 7)
    else:
        a = 5 * (y - (y**2/4))**4 + 1
    return a

```

```python
import math


def f1(y):
    return ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6


def f2(y):
    return 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y


def f3(y):
    return (0.08 - 72 * abs(y**3) -
            33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5)


def f4(y):
    return y**4 + 70 * math.pow(y, 7)


def f5(y):
    return 5 * (y - (y**2 / 4))**4 + 1


def main(y):
    if y < 70:
        return f1(y)
    elif 70 <= y < 158:
        return f2(y)
    elif 158 <= y < 251:
        return f3(y)
    elif 251 <= y < 320:
        return f4(y)
    else:  # y >= 320
        return f5(y)
```

```python
import math


def f(y):
    if y < 70:
        return ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6
    elif y < 158:
        return 1 + (5 * y**2 - y - y**3)**3 + 60 * y
    elif y < 251:
        return (0.08 - 72 * abs(y**3) -
                33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5)
    elif y < 320:
        return y**4 + 70 * y**7
    else:
        return 5 * (y - (y**2 / 4))**4 + 1


def main(y):
    return f(y)
```

```python
import math


def piecewise(cases):
    def decorator(func):
        def wrapper(y):
            for (cond, result) in cases:
                if cond(y):
                    return result(y)
            return func(y)
        return wrapper
    return decorator


@piecewise([
    (lambda y: y < 70, lambda y: ((y**3 / 37) + 1) /
     3 - 44 * (73 * y**3 - 1)**6),
    (lambda y: 70 <= y < 158, lambda y: 1 + (5 * y**2 - y - y**3)**3 + 60 * y),
    (lambda y: 158 <= y < 251, lambda y: 0.08 - 72 *
     abs(y**3) - 33 * math.tan(y**3 / 91 + 41 * y**2 + 76)**5),
    (lambda y: 251 <= y < 320, lambda y: y**4 + 70 * y**7)
])
def main(y):
    return 5 * (y - (y**2 / 4))**4 + 1

```

### 2 способ
```python
import math


def main(y):
    conditions = [
        (lambda x: x < 70, lambda x:
         ((x**3 / 37) + 1) / 3 - 44 * (73 * x**3 - 1)**6),
        (lambda x: 70 <= x < 158, lambda x:
         1 + (5 * x**2 - x - x**3)**3 + 60 * x),
        (lambda x: 158 <= x < 251, lambda x:
         0.08 - 72 * abs(x**3) - 33 * math.tan(x**3 / 91 + 41 * x**2 + 76)**5),
        (lambda x: 251 <= x < 320, lambda x:
         x**4 + 70 * x**7),
        (lambda x: x >= 320, lambda x:
         5 * (x - (x**2 / 4))**4 + 1)
    ]

    return next(result(y) for condition, result in conditions if condition(y))
```

### 3 способ
```python
import math


def main(y):
    def f1():
        return ((y**3 / 37) + 1) / 3 - 44 * (73 * y**3 - 1)**6

    def f2():
        return 1 + math.pow(5 * y**2 - y - y**3, 3) + 60 * y

    def f3():
        return (0.08 - 72 * abs(y**3) - 33 *
                math.tan(y**3 / 91 + 41 * y**2 + 76)**5)

    def f4():
        return y**4 + 70 * math.pow(y, 7)

    def f5():
        return 5 * (y - (y**2/4))**4 + 1

    funcs = {
        range(0, 70): f1,
        range(70, 158): f2,
        range(158, 251): f3,
        range(251, 320): f4,
        range(320, 1000000): f5
    }

    for key in funcs:
        if y in key:
            return funcs[key]()
```
