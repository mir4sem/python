Реализовать функцию для разбора строки, содержащей данные в текстовом формате. Изучить детали формата по приведенным ниже примерам. Результат вернуть в виде списка пар.

Пример 1

Входная строка:

<:{{var 8780 to q(isus)}} {{ var 7664 to q(soon_686) }} {{ var 159 to q(isor_517)}} :>

Разобранный результат:

[('isus', 8780), ('soon_686', 7664), ('isor_517', 159)]
Пример 2

Входная строка:

<: {{var -6573 to q(enbe) }} {{ var -4380 to q(quteri_319) }} {{ var -4676 to q(maed_661)}}{{ var 56 to q(biarra)}}:>

Разобранный результат:

[('enbe', -6573), ('quteri_319', -4380), ('maed_661', -4676), ('biarra', 56)]

```python
import re
 
 
def main(st):
    var = re.findall(r"var\s(-?\d+)", st)
    q = re.findall(r"q\((\w+)\)", st)
    res = []
    for i in range(len(var)):
        res.append((q[i], int(var[i])))
    return res

```
