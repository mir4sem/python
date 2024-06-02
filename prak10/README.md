Реализовать функцию преобразования табличных данных. Входная и выходная таблицы заданы в построчной форме, с помощью списков. Заполненные ячейки имеют строковой тип данных. Пустые ячейки имеют значение None.

Округления производятся стандартно, с помощью функции round.

Над входной таблицей провести ряд преобразований:

1. Удалить пустые столбцы.
2. Разбить один из столбцов по разделителю “!”.
3. Преобразовать содержимое ячеек по примерам.
4. Отсортировать строки по столбцу №1 в измененной таблице.

Примеры табличных преобразований:

Пример 1 Исходная таблица:

1	2	3	4	5
<br>
ranosov24[at]mail.ru	177-139-1982	Y!08-03-02
<br>
socusuk58[at]yandex.ru	779-002-9080	N!22-06-99
<br>
visafanz25[at]rambler.ru	375-940-0750	N!27-02-01
<br>
gozebli25[at]mail.ru	927-916-7669	N!07-09-99

Результат преобразования:

1	2	3	4
<br>
gozebli25	927 916-7669	Нет	07.09.99
<br>
ranosov24	177 139-1982	Да	08.03.02
<br>
socusuk58	779 002-9080	Нет	22.06.99
<br>
visafanz25	375 940-0750	Нет	27.02.01

Пример 2 Исходная таблица:

1	2	3	4	5
<br>
sosimanz90[at]rambler.ru	406-292-7678	Y!26-04-03
<br>
tamerlan22[at]gmail.com	455-760-2014	Y!14-12-04
<br>
svatoslav65[at]mail.ru	929-879-3652	N!08-03-04
<br>
bukko44[at]mail.ru	847-050-1918	Y!28-08-99

Результат преобразования:

1	2	3	4
<br>
bukko44	847 050-1918	Да	28.08.99
<br>
sosimanz90	406 292-7678	Да	26.04.03
<br>
svatoslav65	929 879-3652	Нет	08.03.04
<br>
tamerlan22	455 760-2014	Да	14.12.04

```python
def transform_table(table):
    # Удаление пустых столбцов
    non_empty_columns = [col for col in zip(*table) if any(cell is not None for cell in col)]
    table = [list(row) for row in zip(*non_empty_columns)]

    # Разбиение столбца по разделителю "!"
    for row in table:
        for i, cell in enumerate(row):
            if cell and '!' in cell:
                status, date = cell.split('!')
                row[i] = 'Да' if status == 'Y' else 'Нет'
                row.insert(i + 1, date)

    # Преобразование содержимого ячеек
    for row in table:
        row[0] = row[0].split('[at]')[0]  # Удаление доменной части из email
        row[3] = row[3].replace('-', '.')  # Преобразование даты в формат дд.мм.гг

    # Сортировка строк по столбцу №1
    table = sorted(table[1:], key=lambda x: x[0])

    # Добавление заголовка
    header = ['1', '2', '3', '4']
    table.insert(0, header)

    return table

# Тесты
table1 = [
    ['1', '2', '3', '4', '5'],
    ['ranosov24[at]mail.ru', '177-139-1982', 'Y!08-03-02', None, None],
    ['socusuk58[at]yandex.ru', '779-002-9080', 'N!22-06-99', None, None],
    ['visafanz25[at]rambler.ru', '375-940-0750', 'N!27-02-01', None, None],
    ['gozebli25[at]mail.ru', '927-916-7669', 'N!07-09-99', None, None]
]

table2 = [
    ['1', '2', '3', '4', '5'],
    ['sosimanz90[at]rambler.ru', '406-292-7678', 'Y!26-04-03', None, None],
    ['tamerlan22[at]gmail.com', '455-760-2014', 'Y!14-12-04', None, None],
    ['svatoslav65[at]mail.ru', '929-879-3652', 'N!08-03-04', None, None],
    ['bukko44[at]mail.ru', '847-050-1918', 'Y!28-08-99', None, None]
]

print(transform_table(table1))
print(transform_table(table2))
```

# 1 вариант
![image](https://github.com/mir4sem/python/assets/70198995/0a970ace-0db2-489a-90db-266fd9b8513f)

![image](https://github.com/mir4sem/python/assets/70198995/0847a37d-0b60-44c9-adee-a629221145dc)

```python
def main(table):
    # Удаление дубликатов строк
    seen = set()
    unique_table = []
    for row in table:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_table.append(row)

    # Преобразование содержимого ячеек
    transformed_table = []
    for row in unique_table[1:]:
        email_phone, name = row
        email, phone = email_phone.split('&')
        email = email.replace('[at]', '@')
        
        # Удаляем код страны и скобки из номера телефона
        phone = ''.join(filter(str.isdigit, phone.split(' ', 2)[2]))
        
        name = ' '.join(name.split()[::-1])
        transformed_table.append([email, phone, name])

    # Добавление заголовка
    transformed_table.insert(0, ['1', '2', '3'])

    return transformed_table

# Тесты
table1 = [
    ['1', '2'],
    ['evgenij60[at]yandex.ru&+7 (655) 372-21-12', 'Евгений Безучко'],
    ['evgenij60[at]yandex.ru&+7 (655) 372-21-12', 'Евгений Безучко'],
    ['marat98[at]yandex.ru&+7 (086) 292-72-09', 'Марат Фикяк'],
    ['evgenij60[at]yandex.ru&+7 (655) 372-21-12', 'Евгений Безучко'],
    ['artem85[at]rambler.ru&+7 (254) 314-46-46', 'Артем Бивак']
]

table2 = [
    ['1', '2'],
    ['semuzidi49[at]rambler.ru&+7 (807) 907-52-20', 'Даниил Шемузиди'],
    ['andrej29[at]yandex.ru&+7 (039) 638-52-27', 'Андрей Детян'],
    ['kesanskij86[at]yandex.ru&+7 (004) 321-64-27', 'Тимофей Кесанский'],
    ['kesanskij86[at]yandex.ru&+7 (004) 321-64-27', 'Тимофей Кесанский'],
    ['kesanskij86[at]yandex.ru&+7 (004) 321-64-27', 'Тимофей Кесанский']
]

print(main(table1))
print(main(table2))
```

# 2 вариант
![image](https://github.com/mir4sem/python/assets/70198995/1af89151-4573-43e5-8f2a-cb0a68f2364a)

![image](https://github.com/mir4sem/python/assets/70198995/fbcdcc44-2c1b-4111-a0e4-1e1132b7649a)

