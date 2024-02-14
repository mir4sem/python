## 1 способ
```python
import math


def main(z, y, x):
    result = (((70 * y**3 + x**2 + z) ** 2) -
              (math.exp((x**3 / 20) + 1 + 55 * z) ** 4 -
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
