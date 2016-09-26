from add import *

def test_bitreverse():
    assert bitreverse(0) == 0
    assert bitreverse(0b1001101) == 0b1011001

def test_get_bit():
    assert get_bit(0) == (0,0)
    assert get_bit(1) == (0,1)
    assert get_bit(27) == (13,1)

def test_adder():
    assert adder(0, 0, 0) == (0,0)
    assert adder(0, 1, 0) == (1,0)
    assert adder(1, 0, 0) == (1,0)
    assert adder(1, 1, 0) == (0,1)
    assert adder(0, 0, 1) == (1,0)
    assert adder(0, 1, 1) == (0,1)
    assert adder(1, 0, 1) == (0,1)
    assert adder(1, 1, 1) == (1,1)

def test_add():
    assert add(0, 0) == 0
    assert add(17, 0) == 17
    assert add(0, 23) == 23
    #assert add(100, 100) == 200
    #assert add(123203, 2121) == 125324
