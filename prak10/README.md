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
