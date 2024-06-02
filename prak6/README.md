```python
import math


def main(Xi):
    E = {xi**2 for xi in Xi if -95 <= xi <= 51}
    X = set()
    for xi in Xi:
        if xi < 58:
            x = (xi**3 + xi)
            X.add(x)

    Z = X | E
    sum_result = 0

    for e in E:
        for z in Z:
            temp_result = math.ceil(e / 9) - 7 * z
            sum_result += temp_result

    final_result = sum_result + len(E)

    return final_result

```
