from struct import *


def get_D(data, offset):
    d1 = unpack_from(">q", data, offset)[0]
    offset += 8
    d2 = unpack_from(">b", data, offset)[0]
    offset += 1
    d3 = unpack_from(">B", data, offset)[0]
    offset += 1
    size, adress = unpack_from(">II", data, offset)
    offset += 8
    d4 = []
    for i in range(size):
        d4.append(unpack_from(">b", data, adress + i)[0])
    d5 = unpack_from(">B", data, offset)[0]
    offset += 1
    d6 = unpack_from(">H", data, offset)[0]
    offset += 2
    D = {"D1": d1, "D2": d2, "D3": d3, "D4": d4, "D5": d5, "D6": d6}
    return D, offset


def get_C(data, offset):
    c1 = unpack_from(">f", data, offset)[0]
    offset += 4
    c2 = unpack_from(">f", data, offset)[0]
    offset += 4
    c3 = []
    size, adress = unpack_from(">IH", data, offset)
    offset += 6
    for i in range(size):
        c3.append(unpack_from(">d", data, adress + i * 8)[0])
    c4, offset = get_D(data, offset)
    C = {"C1": c1, "C2": c2, "C3": c3, "C4": c4}
    return C, offset


def get_B(data, offset):
    b1 = unpack_from(">d", data, offset)[0]
    offset += 8
    b2 = unpack_from(">H", data, offset)[0]
    offset += 2
    size, adress = unpack_from(">HI", data, offset)
    offset += 6
    bb = []
    for i in range(size):
        bb.append(unpack_from(">c", data, adress + i)[0])
    b3 = "".join(map(lambda x: x.decode(), bb))
    offset += size
    return {"B1": b1, "B2": b2, "B3": b3}


def get_A(data, offset):
    a1 = unpack_from(">Q", data, offset)[0]
    offset += 8
    a2 = []
    adress = []
    for i in range(4):
        adress = unpack_from(">I", data, offset + i * 4)[0]
        a2.append(get_B(data, adress))
    offset += 16
    a3 = unpack_from(">H", data, offset)[0]
    offset += 2
    a4 = unpack_from(">I", data, offset)[0]
    offset += 4
    a5 = unpack_from(">h", data, offset)[0]
    offset += 2
    a6, offset = get_C(data, offset)
    a7 = unpack_from(">b", data, offset)[0]
    offset += 1
    a8 = unpack_from(">H", data, offset)[0]
    A = {"A1": a1, "A2": a2, "A3": a3, "A4": a4,
         "A5": a5, "A6": a6, "A7": a7, "A8": a8}
    return A


def main(data):
    offset = 4
    return get_A(data, offset)


data = (b'CHGC\x07\x90_\xa2\xa2\xe1\xa7\xb0\x00\x00\x00L\x00\x00\x00_\x00\x00\x00r'
        b'\x00\x00\x00\x84\xa0\x0f,\x1d`N\xdd\xf5<8\xdd\x10\xbej\x95\x14'
        b'\x00\x00\x00\x04\x00\x94\xcdP\xfcEB\x88\x8e\x05\x11\xdc\x00\x00\x00\x02'
        b"\x00\x00\x00\xb4z\x98Z\xa2('vv?\xea\x9co=r\xbd\xfa\xa3{\x00\x02\x00\x00\x00J"
        b'bja?\xec7\xf8\xae\xcbV\xd2\xa3\xac\x00\x03\x00\x00\x00\\owz?\xb5B/\xb1o'
        b'Z`\xe9\xdf\x00\x03\x00\x00\x00okv?\xdb-n0_<xca\x00\x02\x00\x00\x00\x82'
        b'\xbf\xdc\xc6B\xfa\x0ee\x1c?\xca\xd6\x1dLL\x08\x90?\xd6\x0e\x98'
        b'\xf0\x12\x8f\xb4?\xe5)M\x17\xe7\xff\xe2\x04\xbf')
print(main(data))
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
print(ddata == main(data))
