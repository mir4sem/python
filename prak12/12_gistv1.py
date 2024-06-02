from struct import *


FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int64')
    d2, offs = parse(buf, offs, 'uint16')
    return dict(D1=d1, D2=d2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'double')
    c2, offs = parse(buf, offs, 'uint16')
    c3, offs = parse(buf, offs, 'float')
    c4 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'uint8')
        c4.append(val)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint8')
    b2, offs = parse(buf, offs, 'double')
    b3size, offs = parse(buf, offs, 'uint16')
    b3offs, offs = parse(buf, offs, 'uint32')
    b3 = []
    for _ in range(b3size):
        val, b3offs = parse_c(buf, b3offs)
        b3.append(val)
    b4, offs = parse(buf, offs, 'uint8')
    b5, offs = parse_d(buf, offs)
    b6, offs = parse(buf, offs, 'int16')
    b7size, offs = parse(buf, offs, 'uint32')
    b7offs, offs = parse(buf, offs, 'uint32')
    b7 = []
    for _ in range(b7size):
        val, b7offs = parse(buf, b7offs, 'uint8')
        b7.append(val)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7), offs


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse(buf, offs, 'int8')
    a3size, offs = parse(buf, offs, 'uint32')
    a3offs, offs = parse(buf, offs, 'uint16')
    a3 = []
    for _ in range(a3size):
        val, a3offs = parse(buf, a3offs, 'float')
        a3.append(val)
    a4, offs = parse(buf, offs, 'int8')
    a5, offs = parse(buf, offs, 'uint64')
    a6, offs = parse(buf, offs, 'uint64')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def main(stream):
    res, _ = parse_a(stream, 5)
    return res
