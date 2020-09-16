from fib_py import fib_py
from fib_py_cy import fib_py_cy
from fib_cy import fib_cy
from fib_py_double import fib_py_double
from fib_py_cy_double import fib_py_cy_double
from fib_cy_double import fib_cy_double
import timeit
import sys

# pass in Fib number to calculate
n = int(sys.argv[1])

# time each version
t1 = min(timeit.repeat(f"fib_py({n})", number=100000, repeat = 10, setup="from fib_py import fib_py; gc.enable()"))
print(f'Pure python: answer = {fib_py(n)}, time = {t1}, speedup = 1.0')

t = min(timeit.repeat(f"fib_py_cy({n})", number=100000, repeat = 10, setup="from fib_py_cy import fib_py_cy; gc.enable()"))
print(f'Cythonized Python: answer = {fib_py_cy(n)}, time = {t}, speedup = {t1 / t}')

t = min(timeit.repeat(f"fib_cy({n})", number=100000, repeat = 10, setup="from fib_cy import fib_cy; gc.enable()"))
print(f'Typed Cython: answer = {fib_cy(n)}, time = {t}, speedup = {t1 / t}')

t = min(timeit.repeat(f"fib_py_double({n})", number=100000, repeat = 10, setup="from fib_py_double import fib_py_double; gc.enable()"))
print(f'Pure Python (double): answer = {fib_py_double(n)}, time = {t}, speedup = {t1 / t}')

t = min(timeit.repeat(f"fib_py_cy_double({n})", number=100000, repeat = 10, setup="from fib_py_cy_double import fib_py_cy_double; gc.enable()"))
print(f'Cythonized Python (double): answer = {fib_py_cy_double(n)}, time = {t}, speedup = {t1 / t}')

t = min(timeit.repeat(f"fib_cy_double({n})", number=100000, repeat = 10, setup="from fib_cy_double import fib_cy_double; gc.enable()"))
print(f'Typed Cython (double): answer = {fib_cy_double(n)}, time = {t}, speedup = {t1 / t}')
