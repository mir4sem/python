from struct import unpack_from, calcsize  # Импортируем необходимые функции из модуля struct

# Класс для хранения типов данных и их кодов для модуля struct
class Types:
    char = 'c'  # Тип данных: char, код: 'c'
    int8 = 'b'  # Тип данных: int8, код: 'b'
    uint8 = 'B'  # Тип данных: uint8, код: 'B'
    int16 = 'h'  # Тип данных: int16, код: 'h'
    uint16 = 'H'  # Тип данных: uint16, код: 'H'
    int32 = 'i'  # Тип данных: int32, код: 'i'
    uint32 = 'I'  # Тип данных: uint32, код: 'I'
    int64 = 'q'  # Тип данных: int64, код: 'q'
    uint64 = 'Q'  # Тип данных: uint64, код: 'Q'
    float = 'f'  # Тип данных: float, код: 'f'
    double = 'd'  # Тип данных: double, код: 'd'


# Класс для чтения бинарных данных
class BinaryReader:
    def __init__(self, data, offset, order=">"):
        # data - бинарные данные
        # offset - смещение в байтах от начала данных
        # order - порядок байтов (">" - big-endian, "<" - little-endian)
        self.data = data  # Сохраняем бинарные данные
        self.offset = offset  # Сохраняем смещение
        self.order = order  # Сохраняем порядок байтов

    # Метод для перемещения указателя чтения на заданное смещение
    def jump(self, offset):
        return BinaryReader(self.data, offset, self.order)  # Возвращаем новый экземпляр BinaryReader с новым смещением

    # Метод для чтения значения заданного типа данных из текущей позиции
    def read(self, pattern):
        # pattern - строка формата для модуля struct
        data = unpack_from(self.order + pattern, self.data, self.offset)  # Читаем данные из бинарного массива
        self.offset += calcsize(pattern)  # Увеличиваем смещение на размер прочитанных данных
        return data[0]  # Возвращаем первое значение из кортежа


# Функция для чтения структуры D
def read_d(reader: BinaryReader):
    d1 = reader.read(Types.int64)  # Читаем поле D1 типа int64
    d2 = reader.read(Types.uint16)  # Читаем поле D2 типа uint16
    return dict(D1=d1, D2=d2)  # Возвращаем словарь с прочитанными значениями


# Функция для чтения структуры C
def read_c(reader: BinaryReader):
    c1 = reader.read(Types.double)  # Читаем поле C1 типа double
    c2 = reader.read(Types.uint16)  # Читаем поле C2 типа uint16
    c3 = reader.read(Types.float)  # Читаем поле C3 типа float
    c4 = [reader.read(Types.uint8) for _ in range(4)]  # Читаем массив C4 из 4 элементов типа uint8
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)  # Возвращаем словарь с прочитанными значениями


# Функция для чтения структуры B
def read_b(reader: BinaryReader):
    b1 = reader.read(Types.uint8)  # Читаем поле B1 типа uint8
    b2 = reader.read(Types.double)  # Читаем поле B2 типа double
    b3size = reader.read(Types.uint16)  # Читаем размер массива B3 (uint16)
    b3addr = reader.read(Types.uint32)  # Читаем адрес массива B3 (uint32)
    b3reader = reader.jump(b3addr)  # Создаем новый reader, указывающий на адрес массива B3
    b3 = [read_c(b3reader) for _ in range(b3size)]  # Читаем массив структур C (B3)
    b4 = reader.read(Types.uint8)  # Читаем поле B4 типа uint8
    b5 = read_d(reader)  # Читаем структуру D (B5)
    b6 = reader.read(Types.int16)  # Читаем поле B6 типа int16
    b7size = reader.read(Types.uint32)  # Читаем размер массива B7 (uint32)
    b7address = reader.read(Types.uint32)  # Читаем адрес массива B7 (uint32)
    b7reader = reader.jump(b7address)  # Создаем новый reader, указывающий на адрес массива B7
    b7 = [b7reader.read(Types.uint8) for _ in range(b7size)]  # Читаем массив B7 из элементов типа uint8
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)  # Возвращаем словарь с прочитанными значениями


# Функция для чтения структуры A
def read_a(reader: BinaryReader):
    a1 = read_b(reader)  # Читаем структуру B (A1)
    a2 = reader.read(Types.int8)  # Читаем поле A2 типа int8
    a3size = reader.read(Types.uint32)  # Читаем размер массива A3 (uint32)
    a3address = reader.read(Types.uint16)  # Читаем адрес массива A3 (uint16)
    a3reader = reader.jump(a3address)  # Создаем новый reader, указывающий на адрес массива A3
    a3 = [a3reader.read(Types.float) for _ in range(a3size)]  # Читаем массив A3 из элементов типа float
    a4 = reader.read(Types.int8)  # Читаем поле A4 типа int8
    a5 = reader.read(Types.uint64)  # Читаем поле A5 типа uint64
    a6 = reader.read(Types.uint64)  # Читаем поле A6 типа uint64
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)  # Возвращаем словарь с прочитанными значениями


# Главная функция для чтения данных из байтового массива
def main(bytes):
    reader = BinaryReader(bytes, 5, '<')  # Создаем экземпляр BinaryReader с указанием смещения 5 и порядка little-endian
    return read_a(reader)  # Вызываем функцию для чтения структуры A и возвращаем результат
