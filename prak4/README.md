![изображение](https://github.com/mir4sem/python/assets/70198995/f3c8b833-5fa2-4a75-bdb8-2bf2cbd59f32)

## 1 способ
```python
def main(n):
    if n == 0:
        return 0.92
    elif n == 1:
        return 0.79
    else:
        return (main(n-1))**2 - (main(n-2))**3 / 64 - main(n-1) / 63

```

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def main(n):
    if n == 0:
        return 0.92
    elif n == 1:
        return 0.79
    else:
        return (main(n-1))**2 - (main(n-2))**3 / 64 - main(n-1) / 63
```

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def main(n):
    a, b = 0.92, 0.79
    for i in range(2, n+1):
        a, b = b, b**2 - a**3 / 64 - b / 63
    return b

```

## 2 способ
```python
def main(n):
    a, b = 0.92, 0.79
    for i in range(2, n+1):
        a, b = b, b**2 - a**3 / 64 - b / 63
    return b

```

## 3 способ
```python
def main(n):
    results = [0.92, 0.79] + [0] * (n-1)
    for i in range(2, n+1):
        results[i] = results[i-1]**2 - results[i-2]**3 / 64 - results[i-1] / 63
    return results[n]

```
