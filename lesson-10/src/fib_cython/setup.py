from setuptools import setup, Extension
from Cython.Build import cythonize


def main():
    setup(
       name="fibutils_cyth",
       version="3.0.0",
       ext_modules= cythonize(["fibutils_cyth.pyx"])
    )


if __name__ == "__main__":
    main()
