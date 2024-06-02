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


def main(data_string):
    # Удаляем начальные и конечные символы
    data_string = data_string.strip('<:> ')

    # Используем регулярное выражение для поиска всех пар (ключ, значение)
    pattern = r'var\s+(-?\d+)\s+to\s+q\(([^)]+)\)'
    matches = re.findall(pattern, data_string, re.DOTALL)

    # Формируем список пар (ключ, значение)
    result = [(key, int(value)) for value, key in matches]

    return result

# Тесты
data_string1 = "<:{{var 8780 to q(isus)}} {{ var 7664 to q(soon_686) }} {{ var 159 to q(isor_517)}} :>"
data_string2 = "<: {{var -6573 to q(enbe) }} {{ var -4380 to q(quteri_319) }} {{ var -4676 to q(maed_661)}}{{ var 56 to q(biarra)}}:>"
data_string3 = "<:{{var 8780 to q(isus)}} {{ var 7664 to q(soon_686) }} {{ var 159 to\nq(isor_517)}} :>"

print(main(data_string1))  # [('isus', 8780), ('soon_686', 7664), ('isor_517', 159)]
print(main(data_string2))  # [('enbe', -6573), ('quteri_319', -4380), ('maed_661', -4676), ('biarra', 56)]
print(main(data_string3))  # [('isus', 8780), ('soon_686', 7664), ('isor_517', 159)]
```

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

# 1 вариант
Реализовать функцию для разбора строки, содержащей данные в текстовом формате. Изучить детали формата по приведенным ниже примерам. Результат вернуть в виде списка пар.

Пример 1

Входная строка:

<section> |variable cema_58<==2436 |; | variable ones <== -895|;|variable aarbeus_829 <== -7973|; | variable inle <== 2394 |;</section>

    Разобранный результат:

[('cema_58', 2436), ('ones', -895), ('aarbeus_829', -7973), ('inle', 2394)]

Пример 2

Входная строка:

<section>| variable ariin <== -2621 |; | variable requ<==-6108 |;</section>

Разобранный результат:

[('ariin', -2621), ('requ', -6108)]
