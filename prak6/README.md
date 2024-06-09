![image](https://github.com/mir4sem/python/assets/70198995/543c5be6-87eb-4ea6-a351-e6aacc26e68c)

Примеры результатов вычислений:

main({-63, 36, 70, -89, -79, -78, -13, 60, -65}) = 104084288

main({-28, 50, 19, -2, -41, 57, 91, -68, 30, -65}) = 17996431

```python
import math


def main(Xi):
    E = {xi**2 for xi in Xi if -95 <= xi <= 51}
    X = {xi**3 + xi for xi in Xi if xi < 58}

    Z = X.union(E)
    result = 0

    for e in E:
        for z in Z:
            temp_result = math.ceil(e / 9) - 7 * z
            result += temp_result

    final_result = len(E) + result 

    return final_result

print(main({-63, 36, 70, -89, -79, -78, -13, 60, -65})) # 104084288
print(main({-28, 50, 19, -2, -41, 57, 91, -68, 30, -65})) # 17996431
```

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
