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
