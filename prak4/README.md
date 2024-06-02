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
