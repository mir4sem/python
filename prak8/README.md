Реализовать функцию для декодирования данных, содержащих битовые поля. В решении необходимо использовать побитовые операции. Неиспользуемые поля результата должны содержать нулевые биты.

Входные данные:

![image](https://github.com/mir4sem/python/assets/70198995/be2fdc6b-3634-44da-9837-b30c64b2c96f)

Выходные данные:

Кортеж из битовых полей в порядке от младших бит к старшим. Значения битовых полей имеют тип: шестнадцатиричная строка.

Тесты:

main('12930800291')
<br>
('0xa3', '0x5a', '0x4', '0x2b', '0xc')

main('5491355607')
<br>
('0xd7', '0x6f', '0x7', '0x74', '0x5')

main('4385472263')
<br>
('0x7', '0xff', '0x4', '0x56', '0x4')

main('8283508376')
<br>
('0x98', '0x4e', '0x4', '0x2db', '0x7')

### Объъяснение
поле = (число >> смещение) & маска

- поле - это переменная, в которую мы сохраняем извлечённое битовое поле.
- число - это исходное число, из которого мы извлекаем битовое поле.
- смещение - это количество бит, на которое нужно сдвинуть число вправо.
- маска - это двоичное число, которое определяет, какие биты нужно оставить после сдвига.

```python
def main(data):
    num = int(data)
    E1 = num & 0xFF  # смещение 0 (нет), маска 1111 1111
    E2 = (num >> 8) & 0xFF  # смещение 8, маска 1111 1111
    E3 = (num >> 16) & 0x7  # смещение 16, маска 111
    E5 = (num >> 20) & 0x3FF  #  смещение 20, маска 11 1111 1111
    E6 = (num >> 30) & 0xF  # смещение 30
    E1_hex = hex(E1)
    E2_hex = hex(E2)
    E3_hex = hex(E3)
    E5_hex = hex(E5)
    E6_hex = hex(E6)
    return (E1_hex, E2_hex, E3_hex, E5_hex, E6_hex)

```

```python
def main(input_string):
    input_int = int(input_string)
    hex_representation1 = hex(input_int & 0xFF)
    hex_representation2 = hex((input_int >> 8) & 0xFF)
    hex_representation3 = hex((input_int >> 16) & 0x7)
    hex_representation4 = f"0x{((input_int >> 20) & 0x3FF):3x}"
    hex_representation4 = hex_representation4.replace(" ", "")
    hex_representation5 = hex((input_int >> 30) & 0xFF)
    res = (hex_representation1, hex_representation2,
           hex_representation3, hex_representation4, hex_representation5)
    return res

```

# 1 Вариант
![image](https://github.com/mir4sem/python/assets/70198995/596a949b-1417-49f3-985b-6d4000c80c4f)

```python
def main(data):
    # Преобразуем входные строки в целые числа
    T1, T2, T3, T4 = map(int, data)

    # Сдвигаем битовые поля на соответствующие позиции
    T1 <<= 0  # T1 уже на месте
    T2 <<= 4  # Сдвигаем T2 на 3 бита влево
    T3 <<= 5  # Сдвигаем T3 на 5 бит влево
    T4 <<= 12 # Сдвигаем T4 на 11 бит влево

    # Объединяем битовые поля с помощью побитовой операции ИЛИ
    result = T1 | T2 | T3 | T4

    # Преобразуем результат в шестнадцатеричную строку
    return hex(result)

# Тесты
print(main(('1', '1', '55', '0')))  # '0x6f1'
print(main(('12', '1', '27', '2'))) # '0x237c'
print(main(('5', '0', '81', '13'))) # '0xda25'
print(main(('12', '0', '13', '2'))) # '0x21ac'
```
