```python
def f(n):
    if n == 0:
        return 0.92
    elif n == 1:
        return 0.79
    else:
        return (f(n-1))**2 - (f(n-2))**3 / 64 - f(n-1) / 63

```
