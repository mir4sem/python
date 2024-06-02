Реализовать функцию для вычисления дерева решений:

![image](https://github.com/mir4sem/python/assets/70198995/57b59551-b872-4ad1-9cef-7f3c1dcca4c2)

Примеры результатов вычислений:

main(['HAML', 'JSON5', 1971, 'IOKE']) = 5

main(['VHDL', 'JSON5', 1971, 'REBOL']) = 10

main(['HAML', 'TXL', 2001, 'REBOL']) = 1

main(['PERL', 'JSON5', 2001, 'IOKE']) = 6

main(['HAML', 'JSON5', 2001, 'REBOL']) = 2

```python
def x0(x, left, mid, right):
    if x[0] == "HAML":
        return left
    elif x[0] == "PERL":
        return mid
    elif x[0] == "VHDL": 
        return right
        
def x1(x, left, mid, right):
    if x[1] == "METAL":
        return left
    elif x[1] == "TXL":
        return mid
    elif x[1] == "JSON5": 
        return right


def x2(x, left, right):
    if x[2] == 2001:
        return left
    elif x[2] == 1971:
        return right


def x3(x, left, mid, right):
    if x[3] == "E":
        return left
    elif x[3] == "IOKE":
        return mid
    elif x[3] == "REBOL":
        return right


def main(x):
    return x0(x, x2(x, x1(x, 0, 1, 2), x1(x, 3, 4, 5)), 6, x2(x, x3(x, 7, 8, 9), 10))
```
