def mixColumns(a, b, c, d):
    printHex(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    printHex(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    print()

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    return print('{:02x}'.format(val), end=' ')

mixColumns(0x68, 0x95, 0x63, 0xa8) # 0x8e 0x4d 0xa1 0xbc
mixColumns(0x62, 0x5b, 0x85, 0x0c) # 0x9f 0xdc 0x58 0x9d
mixColumns(0x57, 0xbd, 0xc8, 0x68) # 0x01 0x01 0x01 0x01 
mixColumns(0xab, 0xb7, 0x2c, 0x88) # 0xc6 0xc6 0xc6 0xc6 
