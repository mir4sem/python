from struct import *  # Импортируем все функции из модуля struct


def get_D(data, offset):
    """
    Разбирает структуру D из байтовой строки data, начиная с offset.

    Args:
        data: Байтовая строка, содержащая данные.
        offset: Смещение, с которого начинается структура D.

    Returns:
        Словарь, представляющий структуру D, и новое смещение.
    """
    d1 = unpack_from(">q", data, offset)[0]  # Читаем поле D1 (int64)
    offset += 8  # Увеличиваем смещение на 8 байт (размер int64)
    d2 = unpack_from(">b", data, offset)[0]  # Читаем поле D2 (int8)
    offset += 1  # Увеличиваем смещение на 1 байт (размер int8)
    d3 = unpack_from(">B", data, offset)[0]  # Читаем поле D3 (uint8)
    offset += 1  # Увеличиваем смещение на 1 байт (размер uint8)
    size, adress = unpack_from(">II", data, offset)  # Читаем размер и адрес массива D4
    offset += 8  # Увеличиваем смещение на 8 байт (размер двух uint32)
    d4 = []  # Инициализируем пустой список для массива D4
    for i in range(size):  # Читаем элементы массива D4 (int8)
        d4.append(unpack_from(">b", data, adress + i)[0])
    d5 = unpack_from(">B", data, offset)[0]  # Читаем поле D5 (uint8)
    offset += 1  # Увеличиваем смещение на 1 байт (размер uint8)
    d6 = unpack_from(">H", data, offset)[0]  # Читаем поле D6 (uint16)
    offset += 2  # Увеличиваем смещение на 2 байта (размер uint16)
    D = {"D1": d1, "D2": d2, "D3": d3, "D4": d4, "D5": d5,
         "D6": d6}  # Создаем словарь для структуры D
    return D, offset  # Возвращаем словарь и новое смещение


def get_C(data, offset):
    """
    Разбирает структуру C из байтовой строки data, начиная с offset.

    Args:
        data: Байтовая строка, содержащая данные.
        offset: Смещение, с которого начинается структура C.

    Returns:
        Словарь, представляющий структуру C, и новое смещение.
    """
    c1 = unpack_from(">f", data, offset)[0]  # Читаем поле C1 (float)
    offset += 4  # Увеличиваем смещение на 4 байта (размер float)
    c2 = unpack_from(">f", data, offset)[0]  # Читаем поле C2 (float)
    offset += 4  # Увеличиваем смещение на 4 байта (размер float)
    c3 = []  # Инициализируем пустой список для массива C3
    size, adress = unpack_from(">IH", data, offset)  # Читаем размер и адрес массива C3
    offset += 6  # Увеличиваем смещение на 6 байт (размер uint32 и uint16)
    for i in range(size):  # Читаем элементы массива C3 (double)
        c3.append(unpack_from(">d", data, adress + i * 8)[0])
    c4, offset = get_D(data, offset)  # Рекурсивно разбираем структуру D
    C = {"C1": c1, "C2": c2, "C3": c3, "C4": c4}  # Создаем словарь для структуры C
    return C, offset  # Возвращаем словарь и новое смещение


def get_B(data, offset):
    """
    Разбирает структуру B из байтовой строки data, начиная с offset.

    Args:
        data: Байтовая строка, содержащая данные.
        offset: Смещение, с которого начинается структура B.

    Returns:
        Словарь, представляющий структуру B.
    """
    b1 = unpack_from(">d", data, offset)[0]  # Читаем поле B1 (double)
    offset += 8  # Увеличиваем смещение на 8 байт (размер double)
    b2 = unpack_from(">H", data, offset)[0]  # Читаем поле B2 (uint16)
    offset += 2  # Увеличиваем смещение на 2 байта (размер uint16)
    size, adress = unpack_from(">HI", data, offset)  # Читаем размер и адрес массива B3
    offset += 6  # Увеличиваем смещение на 6 байт (размер uint16 и uint32)
    bb = []  # Инициализируем пустой список для массива B3
    for i in range(size):  # Читаем элементы массива B3 (char)
        bb.append(unpack_from(">c", data, adress + i)[0])
    b3 = "".join(map(lambda x: x.decode(), bb))  # Преобразуем массив байтов в строку
    offset += size  # Увеличиваем смещение на размер массива B3
    return {"B1": b1, "B2": b2, "B3": b3}  # Возвращаем словарь для структуры B


def get_A(data, offset):
    """
    Разбирает структуру A из байтовой строки data, начиная с offset.

    Args:
        data: Байтовая строка, содержащая данные.
        offset: Смещение, с которого начинается структура A.

    Returns:
        Словарь, представляющий структуру A.
    """
    a1 = unpack_from(">Q", data, offset)[0]  # Читаем поле A1 (uint64)
    offset += 8  # Увеличиваем смещение на 8 байт (размер uint64)
    a2 = []  # Инициализируем пустой список для массива A2
    adress = []
    for i in range(4):  # Читаем адреса структур B
        adress = unpack_from(">I", data, offset + i * 4)[0]
        a2.append(get_B(data, adress))  # Рекурсивно разбираем структуры B
    offset += 16  # Увеличиваем смещение на 16 байт (размер 4 uint32)
    a3 = unpack_from(">H", data, offset)[0]  # Читаем поле A3 (uint16)
    offset += 2  # Увеличиваем смещение на 2 байта (размер uint16)
    a4 = unpack_from(">I", data, offset)[0]  # Читаем поле A4 (uint32)
    offset += 4  # Увеличиваем смещение на 4 байта (размер uint32)
    a5 = unpack_from(">h", data, offset)[0]  # Читаем поле A5 (int16)
    offset += 2  # Увеличиваем смещение на 2 байта (размер int16)
    a6, offset = get_C(data, offset)  # Рекурсивно разбираем структуру C
    a7 = unpack_from(">b", data, offset)[0]  # Читаем поле A7 (int8)
    offset += 1  # Увеличиваем смещение на 1 байт (размер int8)
    a8 = unpack_from(">H", data, offset)[0]  # Читаем поле A8 (uint16)
    A = {"A1": a1, "A2": a2, "A3": a3, "A4": a4,
         "A5": a5, "A6": a6, "A7": a7, "A8": a8}  # Создаем словарь для структуры A
    return A  # Возвращаем словарь


def main(data):
    """
    Основная функция, разбирающая данные.

    Args:
        data: Байтовая строка, содержащая данные.

    Returns:
        Словарь, представляющий структуру A.
    """
    offset = 4  # Начальное смещение (после сигнатуры "CHGC")
    return get_A(data, offset)  # Разбираем структуру A


data = (b'CHGC\x07\x90_\xa2\xa2\xe1\xa7\xb0\x00\x00\x00L\x00\x00\x00_\x00\x00\x00r'
        b'\x00\x00\x00\x84\xa0\x0f,\x1d`N\xdd\xf5<8\xdd\x10\xbej\x95\x14'
        b'\x00\x00\x00\x04\x00\x94\xcdP\xfcEB\x88\x8e\x05\x11\xdc\x00\x00\x00\x02'
        b"\x00\x00\x00\xb4z\x98Z\xa2('vv?\xea\x9co=r\xbd\xfa\xa3{\x00\x02\x00\x00\x00J"
        b'bja?\xec7\xf8\xae\xcbV\xd2\xa3\xac\x00\x03\x00\x00\x00\\owz?\xb5B/\xb1o'
        b'Z`\xe9\xdf\x00\x03\x00\x00\x00okv?\xdb-n0_<xca\x00\x02\x00\x00\x00\x82'
        b'\xbf\xdc\xc6B\xfa\x0ee\x1c?\xca\xd6\x1dLL\x08\x90?\xd6\x0e\x98'
        b'\xf0\x12\x8f\xb4?\xe5)M\x17\xe7\xff\xe2\x04\xbf')
print(main(data))  # Выводим результат разбора
ddata = {'A1': 545040707033868208,
         'A2': [{'B1': 0.8315960121307733, 'B2': 41851, 'B3': 'vv'},
                {'B1': 0.8818324483824773, 'B2': 41900, 'B3': 'bja'},
                {'B1': 0.08304117280872836, 'B2': 59871, 'B3': 'owz'},
                {'B1': 0.42464785312490205, 'B2': 25441, 'B3': 'kv'}],
         'A3': 40975,
         'A4': 740122702,
         'A5': -8715,
         'A6': {'C1': 0.01128317415714264,
                'C2': -0.229084312915802,
                'C3': [-0.4496009294467329,
                       0.20965925431670884,
                       0.3446409553964671,
                       0.6612916438025389],
                'C4': {'D1': -3652141923398283771,
                       'D2': 17,
                       'D3': 220,
                       'D4': [4, -65],
                       'D5': 122,
                       'D6': 39002}},
         'A7': -94,
         'A8': 10279}
print(ddata == main(data))  # Сравниваем результат разбора с ожидаемым
