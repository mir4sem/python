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
