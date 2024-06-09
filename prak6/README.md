![image](https://github.com/mir4sem/python/assets/70198995/02055f93-030a-43d0-a2b8-abf3ede72fa7)

```python
import math

def main(Theta):
    Psi = {
        theta
        for theta in Theta
        if theta <= 54
    }
    
    X = {
        math.ceil(psi / 4) - psi
        for psi in Psi
        if -66 < psi <= 52
    }
        
    Delta = {
        abs(theta) - math.floor(theta / 5)
        for theta in Theta
        if -64 <= theta < 41
    }
    
    N = {
        delta**3 + chi
        for delta in Delta
        for chi in X
        if delta > chi
    }

    sum_X = sum(X)
    sum_XN = sum(
        chi * nu
        for chi in X
        for nu in N
    )
    
    xi = sum_X + sum_XN
    return xi

Theta1 = {98, 69, -90, 41, 74, 46, 25, -70, -67, 62}
Theta2 = {-63, -6, 70, -20, -16, -14, 83, -40, -70, -97}

print(main(Theta1)) # -1961358
print(main(Theta2)) # 398647205
```

![image](https://github.com/mir4sem/python/assets/70198995/44d68119-5c52-40a9-87a1-43325004435b)

```python
import math

def main(T):
    E = {
        math.ceil(tau / 2)
        for tau in T
        if -72 <= tau or tau <= 48
    }

    O = T.union(E)

    K = {
        abs(epsilon)
        for epsilon in E
        if -66 < epsilon < 45
    }

    Υ = {
        o for o in O
        if -47 < o <= -6
    }

    sum_K = sum(
        2 * kappa
        for kappa in K
    )

    sum_KY = sum(
        kappa**2 - nu % 3
        for kappa in K
        for nu in Υ
    )
    
    phi = sum_K + sum_KY
    
    return phi

# Example usage
T1 = {-93, -92, -91, 68, -52, -18, -49, 19, -37}
T2 = {-62, 35, 6, 79, 17, -73, 88, 26, -67}

print(main(T1))  # 49762
print(main(T2))  # 22831
```

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
