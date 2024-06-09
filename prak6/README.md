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

![image](https://github.com/mir4sem/python/assets/70198995/a10a054f-f629-494f-aaa8-02664083a65b)

```python
import math

def main(Θ):
    B = {
        theta + 2 * theta
        for theta in Θ
        if -58 <= theta < 5
    }

    Υ = {
        math.floor(beta / 2)
        for beta in B
        if -98 < beta < -27
    }

    Λ = {
        9 * theta + 4 * theta
        for theta in Θ
        if -57 < theta <= 81
    }

    Z = {
        lam * v
        for lam in Λ
        for v in Υ
        if lam < v
    }

    rho = sum(5*v for v in Υ) + sum(abs(v) + zeta**2 for v in Υ for zeta in Z)

    return rho

# Пример использования
Θ1 = {-96, -29, -58, 41, 74, 79, 50, 85, -42, -4} # 857549176
Θ2 = {32, -32, -61, -60, -85, 49, 52, -10, 91, 28} # 882922122

print(main(Θ1)) 
print(main(Θ2)) 
```

![image](https://github.com/mir4sem/python/assets/70198995/08085229-ccea-4ecf-8617-724fb39523dd)

```python
import math
import numpy as np

def main(B):
    Δ = {
        math.ceil(beta / 2) + 8 * beta
        for beta in B
        if beta >= 5
    }

    X = {
        abs(beta)
        for beta in B
        if beta < 87 or beta >= -27
    }

    I = Δ.union(X)

    Z = {
        math.floor(chi / 3) - iota
        for chi in X
        for iota in I
        if chi <= iota
    }

    union_I_Z = I.union(Z)
    lenIZ = len(union_I_Z)

    PROD = np.prod([
        zeta % 3
        for zeta in Z
    ])

    result = lenIZ + PROD

    return result

B1 = {97, -28, 9, 44, 12, -82, 51, 62, -67, -1}
B2 = {32, 75, -50, 16, -79, 49, 22, 59, -68}

print(main(B1)) # 108
print(main(B2)) # 96
```

![image](https://github.com/mir4sem/python/assets/70198995/ecd5833c-ea5b-4feb-874d-c37169fdae3c)

```python
import math
import numpy as np

def main(Δ):
    X = {
        delta
        for delta in Δ
        if -40 < delta <= 93
    }

    P = {
        delta**2
        for delta in Δ
        if -28 <= delta <= 95
    }

    Λ = X.union(P)

    product_P_Λ = len(P) * len(Λ)

    tau = product_P_Λ + sum(rho * lam for rho in P for lam in Λ)

    return tau


B1 = {1, -23, 74, 10, -18, 80, 18, -70, -66} # 166418002
B2 = {32, 64, 96, -96, 68, 98, 69, -81, -39, 29} # 238921929

print(main(B1)) 
print(main(B2))
```

![image](https://github.com/mir4sem/python/assets/70198995/543c5be6-87eb-4ea6-a351-e6aacc26e68c)

```python
import math


def main(Xi):
    E = {xi**2 for xi in Xi if -95 <= xi <= 51}
    X = {xi**3 + xi for xi in Xi if xi < 58}

    Z = X.union(E)


    final_result = len(E) + sum(math.ceil(e / 9) - 7 * z for e in E for z in Z) 

    return final_result

print(main({-63, 36, 70, -89, -79, -78, -13, 60, -65})) # 104084288
print(main({-28, 50, 19, -2, -41, 57, 91, -68, 30, -65})) # 17996431
```

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
