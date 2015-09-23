from stack import Stack

OCTAL_BASE = 8
DECIMAL_BASE = 10
BINARY_BASE = 2
HEX_BASE = 16

def test_fn():
    given_decimal_num = 112
    assert fn(given_decimal_num, OCTAL_BASE) == 160

    given_decimal_num = 3
    assert fn(given_decimal_num, BINARY_BASE) == 11

    given_decimal_num = 256
    assert fn(given_decimal_num, HEX_BASE) == 100


def fn(decimal_num, base):
    rem = Stack()

    while decimal_num >= base:
        rem.push(decimal_num % base)
        decimal_num = decimal_num / base

    rem.push(decimal_num)

    num_in_given_base = ''
    while not rem.is_empty():
        num_in_given_base += str(rem.pop())

    num_in_given_base_int = int(num_in_given_base)
    print(num_in_given_base_int)
    return num_in_given_base_int


test_fn()

