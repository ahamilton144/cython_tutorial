from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(['fib_py_cy.py', 'fib_cy.pyx', 'fib_py_cy_double.py', 'fib_cy_double.pyx'],
                                annotate=True, language_level=3))
