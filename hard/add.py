
# Add two numbers without using addition operators

def get_bit(n):
    bit = n & 1
    return (n >> 1), bit

def adder(ab, bb, cy_in):
    if cy_in == 0:
        if ab == bb == 0:
            return 0,0
        elif ab == bb == 1:
            return 0,1
        else:
            return 1,0
    else:
        if ab == bb == 0:
            return 1,0
        elif ab == bb == 1:
            return 1,1
        else:
            return 0,1

def bitreverse(c):
    r = 0
    while True:
        c, bit = get_bit(c)
        r = (r << 1) | bit
        if c == 0: break
    return r

def add(a, b):
    assert type(a) == type(b) == int
    c = 0
    carry = 0
    while True:
        a, a_bit = get_bit(a)
        b, b_bit = get_bit(b)
        c_bit, carry = adder(a_bit, b_bit, carry)
        c = (c << 1) | c_bit
        if a == b == 0: break
    if carry:
        c = (c << 1) | carry
    print("crev", c)
    return bitreverse(c)



