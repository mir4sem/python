## 1 способ
```python
import math


def main(z, y, x):
    result = (((70 * y**3 + x**2 + z) ** 2) -
              (math.exp((x**3 / 20) + 1 + 55 * z) ** 4 -
              ((y**3 - 48) ** 5 / 73)))
    return result

```

## 2 способ
```python
from math import exp


def main(z, y, x):
    result = (((70 * y**3 + x**2 + z) ** 2) -
              (exp((x**3 / 20) + 1 + 55 * z) ** 4 -
              ((y**3 - 48) ** 5 / 73)))
    return result

```

## 3 способ
```python
import math


def main(z, y, x):
    return (((70 * y**3 + x**2 + z) ** 2) -
            (math.exp((x**3 / 20) + 1 + 55 * z) ** 4 -
             ((y**3 - 48) ** 5 / 73)))

```

```python
import math


def main(z, y, x):
    return (((70 * math.pow(y, 3) + math.pow(x, 2) + z) ** 2) -
            (math.exp((math.pow(x, 3) / 20) + 1 + 55 * z) ** 4 -
             ((math.pow(y, 3) - 48) ** 5 / 73)))

```

```python
import math


def main(z, y, x):
    return (((70 * y**3 + x**2 + z) ** 2) -
            (math.pow(math.e, ((x**3 / 20) + 1 + 55 * z)) ** 4 -
            ((y**3 - 48) ** 5 / 73)))

```

## 4 способ
```python
from math import exp


def main(z, y, x):
    return (((70 * y**3 + x**2 + z) ** 2) -
            (exp((x**3 / 20) + 1 + 55 * z) ** 4 -
             ((y**3 - 48) ** 5 / 73)))

```
