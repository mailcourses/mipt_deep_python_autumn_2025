import random
import cffi


def test_sum():
    ffi = cffi.FFI()
    lib = ffi.dlopen("../fib_ctypes/libfibutils.so")

    ffi.cdef("int sum(int *arr, int len);")

    arr = random.sample(list(range(-1000, 2000)), 100)
    c_arr = ffi.new("int[]", arr)

    result = lib.sum(c_arr, len(arr))
    print(f"{result=}, {sum(arr)=}")


def test_compile():
    ffi = cffi.FFI()

    ffi.cdef("int mult(int a, int b, int c);")

    ffi.set_source(
        "multutil",
        """
        int mult(int a, int b, int c)
        {
            return a * b * c;
        }
        """,
    )
    ffi.compile()


    import multutil

    print(multutil.lib.mult(2, 5, 19), 2 * 5 * 19)


if __name__ == "__main__":
    test_sum()
    test_compile()
