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
