import struct


def main(data):
    if data[:4] != b'CHGC':
        raise ValueError("Invalid signature")
    offset = 4
    A1, = struct.unpack_from('>Q', data, offset)
    offset += 8
    A2_offsets = struct.unpack_from('>4I', data, offset)
    offset += 16
    A3, = struct.unpack_from('>H', data, offset)
    offset += 2
    A4, = struct.unpack_from('>I', data, offset)
    offset += 4
    A5, = struct.unpack_from('>h', data, offset)
    offset += 2
    C1, C2 = struct.unpack_from('>ff', data, offset)
    offset += 8
    C3_size, C3_offset = struct.unpack_from('>IH', data, offset)
    offset += 6
    D1, D2, D3 = struct.unpack_from('>qBb', data, offset)
    offset += 10
    D4_size, D4_offset = struct.unpack_from('>II', data, offset)
    offset += 8
    D5, = struct.unpack_from('>B', data, offset)
    offset += 1
    D6, = struct.unpack_from('>H', data, offset)
    offset += 2
    C3 = list(struct.unpack_from(f'>{C3_size}d', data, C3_offset))
    D4 = list(struct.unpack_from(f'>{D4_size}b', data, D4_offset))
    A6 = {
        'C1': C1,
        'C2': C2,
        'C3': C3,
        'C4': {
            'D1': D1,
            'D2': D2,
            'D3': D3,
            'D4': D4,
            'D5': D5,
            'D6': D6,
        }
    }
    A7, = struct.unpack_from('>b', data, offset)
    offset += 1
    A8, = struct.unpack_from('>H', data, offset)
    offset += 2
    A2 = []
    for addr in A2_offsets:
        B1, B2 = struct.unpack_from('>dH', data, addr)
        B3_size, B3_offset = struct.unpack_from('>HI', data, addr + 10)
        B3 = struct.unpack_from(f'>{B3_size}s',
                                data, B3_offset)[0].decode('ascii')
        A2.append({
            'B1': B1,
            'B2': B2,
            'B3': B3,
        })

    return {
        'A1': A1,
        'A2': A2,
        'A3': A3,
        'A4': A4,
        'A5': A5,
        'A6': A6,
        'A7': A7,
        'A8': A8,
    }
