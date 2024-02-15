CТЕПЕРЬ ЧЕРЕЗ pow!

## 1 способ
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
        return a * b
    elif 251 <= y < 320:
        a = y**4 + 70 * pow(y, 7)
        return a
    return 5 * (y - (y**2/4))**4 + 1

```
