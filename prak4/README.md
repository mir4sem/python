```python
def main(n):
    if n == 0:
        return 0.92
    elif n == 1:
        return 0.79
    else:
        return (main(n-1))**2 - (main(n-2))**3 / 64 - main(n-1) / 63

```
