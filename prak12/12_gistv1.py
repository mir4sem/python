from struct import *  # Импортируем все функции из модуля struct

# Словарь, связывающий имена типов данных с их кодами для модуля struct
FMT = dict(
    char='c',  # Тип данных: char, код: 'c'
    int8='b',  # Тип данных: int8, код: 'b'
    uint8='B',  # Тип данных: uint8, код: 'B'
    int16='h',  # Тип данных: int16, код: 'h'
    uint16='H',  # Тип данных: uint16, код: 'H'
    int32='i',  # Тип данных: int32, код: 'i'
    uint32='I',  # Тип данных: uint32, код: 'I'
    int64='q',  # Тип данных: int64, код: 'q'
    uint64='Q',  # Тип данных: uint64, код: 'Q'
    float='f',  # Тип данных: float, код: 'f'
    double='d'  # Тип данных: double, код: 'd'
)


# Функция для разбора значения заданного типа данных из буфера
def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]  # Получаем код типа данных из словаря FMT
    size = calcsize(pattern)  # Вычисляем размер типа данных
    value = unpack_from(order + pattern, buf, offs)[0]  # Распаковываем значение из буфера
    return value, offs + size  # Возвращаем значение и новое смещение


# Функция для разбора структуры D
def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int64')  # Читаем поле D1 типа int64
    d2, offs = parse(buf, offs, 'uint16')  # Читаем поле D2 типа uint16
    return dict(D1=d1, D2=d2), offs  # Возвращаем словарь с прочитанными значениями и новое смещение


# Функция для разбора структуры C
def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'double')  # Читаем поле C1 типа double
    c2, offs = parse(buf, offs, 'uint16')  # Читаем поле C2 типа uint16
    c3, offs = parse(buf, offs, 'float')  # Читаем поле C3 типа float
    c4 = []  # Инициализируем пустой список для поля C4
    for _ in range(4):  # Цикл для чтения 4 элементов массива C4
        val, offs = parse(buf, offs, 'uint8')  # Читаем элемент массива типа uint8
        c4.append(val)  # Добавляем элемент в список c4
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs  # Возвращаем словарь с прочитанными значениями и новое смещение


# Функция для разбора структуры B
def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint8')  # Читаем поле B1 типа uint8
    b2, offs = parse(buf, offs, 'double')  # Читаем поле B2 типа double
    b3size, offs = parse(buf, offs, 'uint16')  # Читаем размер массива B3 (uint16)
    b3offs, offs = parse(buf, offs, 'uint32')  # Читаем смещение массива B3 (uint32)
    b3 = []  # Инициализируем пустой список для массива B3
    for _ in range(b3size):  # Цикл для чтения элементов массива B3
        val, b3offs = parse_c(buf, b3offs)  # Читаем структуру C (элемент массива B3)
        b3.append(val)  # Добавляем структуру C в список b3
    b4, offs = parse(buf, offs, 'uint8')  # Читаем поле B4 типа uint8
    b5, offs = parse_d(buf, offs)  # Читаем структуру D (B5)
    b6, offs = parse(buf, offs, 'int16')  # Читаем поле B6 типа int16
    b7size, offs = parse(buf, offs, 'uint32')  # Читаем размер массива B7 (uint32)
    b7offs, offs = parse(buf, offs, 'uint32')  # Читаем смещение массива B7 (uint32)
    b7 = []  # Инициализируем пустой список для массива B7
    for _ in range(b7size):  # Цикл для чтения элементов массива B7
        val, b7offs = parse(buf, b7offs, 'uint8')  # Читаем элемент массива типа uint8
        b7.append(val)  # Добавляем элемент в список b7
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7), offs  # Возвращаем словарь с прочитанными значениями и новое смещение


# Функция для разбора структуры A
def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)  # Читаем структуру B (A1)
    a2, offs = parse(buf, offs, 'int8')  # Читаем поле A2 типа int8
    a3size, offs = parse(buf, offs, 'uint32')  # Читаем размер массива A3 (uint32)
    a3offs, offs = parse(buf, offs, 'uint16')  # Читаем смещение массива A3 (uint16)
    a3 = []  # Инициализируем пустой список для массива A3
    for _ in range(a3size):  # Цикл для чтения элементов массива A3
        val, a3offs = parse(buf, a3offs, 'float')  # Читаем элемент массива типа float
        a3.append(val)  # Добавляем элемент в список a3
    a4, offs = parse(buf, offs, 'int8')  # Читаем поле A4 типа int8
    a5, offs = parse(buf, offs, 'uint64')  # Читаем поле A5 типа uint64
    a6, offs = parse(buf, offs, 'uint64')  # Читаем поле A6 типа uint64
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs  # Возвращаем словарь с прочитанными значениями и новое смещение


# Главная функция для разбора данных из потока
def main(stream):
    res, _ = parse_a(stream, 5)  # Вызываем функцию для разбора структуры A с начальным смещением 5
    return res  # Возвращаем результат разбора
