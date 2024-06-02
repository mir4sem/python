![изображение](https://github.com/mir4sem/python/assets/70198995/7d6addd5-2457-4298-93f3-907653b05a87)

$f\overrightarrow{z},\overrightarrow{x},\overrightarrow{y} = \sum_{i+1}^{n} \left (z_{n+1-i}^{3} - y_{n+1-[i/2]}^{2}-81x_{[i/2]}\right) ^ 6 $
 
Примеры результатов вычислений:

f([0.24, -0.09],
[-0.87, -0.26],
[-0.97, 0.1]) ≈ 4.68e+11
f([0.23, 0.64],
[0.54, -0.48],
[-0.01, -0.4]) ≈ 3.99e-01
f([0.3, 0.92],
[0.44, 0.68],
[-0.21, -0.75]) ≈ 4.78e+07
f([-0.86, 0.63],
[0.02, 0.91],
[0.92, -0.99]) ≈ 3.72e+11
f([-0.21, 0.82],
[1.0, 0.94],
[0.97, -0.43]) ≈ 4.93e+11

```python
from math import floor


def main(z, y, x):
    n = len(z)
    result = 0
    for i in range(1, n + 1):
        z_index = n - i
        y_index = n - floor((i - 1) / 2) - 1
        x_index = floor((i - 1) / 2)
        result += (z[z_index] ** 3 - y[y_index] ** 2 - 81 * x[x_index]) ** 6
    return result

```
