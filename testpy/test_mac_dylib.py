from ctypes import CDLL


LIBC = CDLL("build/libmylib.dylib")


def test_mylib():
    res = LIBC.add(1, 2)

    print(f"add(1, 2) == {res}")

    assert(res == 3)
    assert(res > 0)
    assert(res < 5)


def main():
    test_mylib()


if __name__ == '__main__':
    main()
