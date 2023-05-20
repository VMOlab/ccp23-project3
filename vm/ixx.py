"""
VMO Lab.
Fixed length integers. ixx.
"""
from .exceptions import *


def larger_type(x, y):
    """ Find the larger type """
    if not issubclass(type(x), ixx) or not issubclass(type(y), ixx):
        raise Exception('Illegal Type')

    if x.BIT_LENGTH > y.BIT_LENGTH:
        return type(x)
    else:
        return type(y)


def zext(bitvec, length):
    """ Zero-Extension (in-place) """
    while len(bitvec) < length:
        bitvec.append(0)


def sext(bitvec, length):
    """ Signed-Extension (in-place) """
    msb = bitvec[-1]
    while len(bitvec) < length:
        bitvec.append(msb)


class ixx:
    """
    Base Class for the Fixed Length Integers.
    """
    BIT_LENGTH = 32

    def __init__(self, value):
        # LSB: index 0, MSB: index 31
        self.__bitvec = ()
        is_minus = False

        bitlist = []
        if type(value) == int:
            # TODO
            pass
        elif type(value) == list:
            # TODO
            pass
        elif issubclass(type(value), ixx):
            # TODO
            pass
        else:
            # TODO
            pass

    def __getitem__(self, idx):
        return self.__bitvec[idx]

    def __repr__(self):
        return f'{int(self)}: {"".join(str(b) for b in self.__bitvec[::-1])}'

    def __int__(self):
        # TODO
        pass

    def __str__(self):
        return str(int(self))

    def __pos__(self):
        return self

    def __neg__(self):
        # TODO
        pass

    def __add__(self, other):
        # TODO
        pass

    def __sub__(self, other):
        # TODO
        pass

    def __mul__(self, other):
        # TODO
        pass

    def __truediv__(self, other):
        # TODO
        pass

    def __abs__(self):
        # TODO
        pass

    def __bool__(self):
        # TODO
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __ne__(self, other):
        # TODO
        pass

    def __lt__(self, other):
        # TODO
        pass

    def __gt__(self, other):
        # TODO
        pass

    def __le__(self, other):
        # TODO
        pass

    def __ge__(self, other):
        # TODO
        pass


class i8(ixx):
    BIT_LENGTH = 8


class i16(ixx):
    BIT_LENGTH = 16


class i32(ixx):
    BIT_LENGTH = 32


class i64(ixx):
    BIT_LENGTH = 64


if __name__ == '__main__':
    """
    Test as you want.
    """
    x = i32(-999)
    y = i32(10)

    print(x)
    print(y)

    z = x / y

    print(f'{z}: {type(z)}')
