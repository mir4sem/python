![image](https://github.com/mir4sem/python/assets/70198995/8ecba489-f697-4710-ab2d-5657bcc531bb)

```python
def x0(x, left, right):
    if x[0] == "JSON5":
        return left
    elif x[0] == "IOKE":
        return right

def x1(x, left, mid, right):
    if x[1] == "VHDL":
        return left
    elif x[1] == "RHTML":
        return mid
    elif x[1] == "RED":
        return right


def x2(x, left, right):
    if x[2] == "UNO":
        return left
    elif x[2] == "RAGEL":
        return right


def x3(x, left, mid, right):
    if x[3] == "QMAKE":
        return left
    elif x[3] == "CSV":
        return mid
    elif x[3] == "GRACE":
        return right


def main(x):
    return x2(x, x3(x, x1(x, 0, 1, 2), x1(x, 3, 4, 5), 6), x1(x, x0(x, 7, 8), x3(x, 9, 10, 11), 12))

print(main(['IOKE', 'RED', 'RAGEL', 'CSV'])) # 12
print(main(['JSON5', 'VHDL', 'UNO', 'CSV'])) # 3
print(main(['JSON5', 'VHDL', 'RAGEL', 'GRACE'])) # 7
print(main(['IOKE', 'VHDL', 'UNO', 'QMAKE'])) # 0
print(main(['JSON5', 'RHTML', 'UNO', 'CSV'])) # 4
```

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
    return x0(x, x2(x, x1(x, 0, 1, 2),
                    x1(x, 3, 4, 5)), 6, x2(x, x3(x, 7, 8, 9), 10))

```

### Когнитивно сложный код 12 > 10
```python
def main(x):
    decision_tree = {
        'HAML': {
            2001: {
                'METAL': 0,
                'TXL': 1,
                'JSON5': 2
            },
            1971: {
                'METAL': 3,
                'TXL': 4,
                'JSON5': 5
            }
        },
        'PERL': 6,
        'VHDL': {
            2001: {
                'E': 7,
                'IOKE': 8,
                'REBOL': 9
            },
            1971: 10
        }
    }

    current_node = decision_tree.get(x[0], None)
    if current_node is None:
        return None

    if isinstance(current_node, dict):
        current_node = current_node.get(x[2], None)
        if current_node is None:
            return None

    if isinstance(current_node, dict):
        current_node = current_node.get(x[1], None)
        if current_node is None:
            return None

    if isinstance(current_node, dict):
        current_node = current_node.get(x[3], None)
        if current_node is None:
            return None

    return current_node if isinstance(current_node, int) else None
```
