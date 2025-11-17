import ctypes
import random


def test_sum():
    libfib = ctypes.CDLL("./libfibutils.so")
    libfib.sum.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)

    arr = random.sample(list(range(-1000, 2000)), 100)

    arr_len = len(arr)
    arr_type = ctypes.c_int * arr_len

    result = int(libfib.sum(arr_type(*arr), ctypes.c_int(arr_len)))
    print(f"{result=}, {sum(arr)=}")


def test_strstr():
    libc = ctypes.CDLL(None)
    libc.strstr.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
    libc.strstr.restype = ctypes.c_char_p

    print(f"{libc.strstr(b'qwerty', b'rt')=}")
    print(f"{libc.strstr(b'qwerty', b'q')=}")
    print(f"{libc.strstr(b'qwerty', b'ty')=}")
    print(f"{libc.strstr(b'qwerty', b'asd')=}")


if __name__ == "__main__":
    test_sum()
    test_strstr()
