import time
import ctypes

import cffi
from fib_native import fib_rec_py, fib_iter_py
from fibutils_c_api import fib_rec_c_api, fib_iter_c_api
from fibutils_cyth import fib_rec_cyth, fib_iter_cyth


def calc_fib_native(n_rec, n_iter):
    t1 = time.time()
    result = fib_rec_py(n_rec)
    t2 = time.time()
    print(f"[fib_rec_py] {result=}, time={t2 - t1}")

    t1 = time.time()
    result = fib_iter_py(n_iter)
    t2 = time.time()
    print(f"[fib_iter_py] {result=}, time={t2 - t1}")


def calc_fib_ctypes(n_rec, n_iter):
    libfib = ctypes.CDLL("./fib_ctypes/libfibutils.so")
    libfib.fib_rec_c.argtypes = (ctypes.c_int,)
    libfib.fib_rec_c.restype = ctypes.c_int
    libfib.fib_iter_c.argtypes = (ctypes.c_int,)
    libfib.fib_iter_c.restype = ctypes.c_int

    t1 = time.time()
    result = libfib.fib_rec_c(n_rec)
    t2 = time.time()
    print(f"[fib_rec_ctypes] {result=}, time={t2 - t1}")

    t1 = time.time()
    result = libfib.fib_iter_c(n_iter)
    t2 = time.time()
    print(f"[fib_iter_ctypes] {result=}, time={t2 - t1}")


def calc_fib_cffi(n_rec, n_iter):
    ffi = cffi.FFI()
    lib = ffi.dlopen("./fib_ctypes/libfibutils.so")

    ffi.cdef("int fib_rec_c(int n);")
    ffi.cdef("int fib_iter_c(int n);")

    t1 = time.time()
    result = lib.fib_rec_c(n_rec)
    t2 = time.time()
    print(f"[fib_rec_cffi] {result=}, time={t2 - t1}")

    t1 = time.time()
    result = lib.fib_iter_c(n_iter)
    t2 = time.time()
    print(f"[fib_iter_cffi] {result=}, time={t2 - t1}")


def calc_fib_c_api(n_rec, n_iter):
    t1 = time.time()
    result = fib_rec_c_api(n_rec)
    t2 = time.time()
    print(f"[fib_rec_c_api] {result=}, time={t2 - t1}")

    t1 = time.time()
    result = fib_iter_c_api(n_iter)
    t2 = time.time()
    print(f"[fib_iter_c_api] {result=}, time={t2 - t1}")


def calc_fib_cyth(n_rec, n_iter):
    t1 = time.time()
    result = fib_rec_cyth(n_rec)
    t2 = time.time()
    print(f"[fib_rec_cyth] {result=}, time={t2 - t1}")

    t1 = time.time()
    result = fib_iter_cyth(n_iter)
    t2 = time.time()
    print(f"[fib_iter_cyth] {result=}, time={t2 - t1}")


def run():
    n_rec, n_iter = 39, 45

    calc_fib_native(n_rec, n_iter)
    print("-" * 50, "\n")

    calc_fib_ctypes(n_rec, n_iter)
    print("-" * 50, "\n")

    calc_fib_cffi(n_rec, n_iter)
    print("-" * 50, "\n")

    calc_fib_c_api(n_rec, n_iter)
    print("-" * 50, "\n")

    calc_fib_cyth(n_rec, n_iter)
    print("-" * 50, "\n")


if __name__ == "__main__":
    run()
