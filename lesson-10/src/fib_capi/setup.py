from setuptools import setup, Extension


def main():
    setup(
       name="fibutils_c_api",
       version="1.0.0",
       ext_modules=[Extension("fibutils_c_api", ["fibutils_capi.c"])],
    )


if __name__ == "__main__":
    main()
