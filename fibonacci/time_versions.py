from fib_py import fib_py
from fib_py_cy import fib_py_cy
from fib_cy import fib_cy
from fib_py_double import fib_py_double
from fib_py_cy_double import fib_py_cy_double
from fib_cy_double import fib_cy_double
import timeit

n = 40
t1 = timeit.timeit(f"fib_py({n})", number=1000000, setup="from fib_py import fib_py")
print(f'Pure python: answer = {fib_py(n)}, time = {t1}, speedup = 1.0')

t = timeit.timeit(f"fib_py_cy({n})", number=1000000, setup="from fib_py_cy import fib_py_cy")
print(f'Cythonized python: answer = {fib_py_cy(n)}, time = {t}, speedup = {t1 / t}')

t = timeit.timeit(f"fib_cy({n})", number=1000000, setup="from fib_cy import fib_cy")
print(f'Typed Cython: answer = {fib_cy(n)}, time = {t}, speedup = {t1 / t}')

t = timeit.timeit(f"fib_py_double({n})", number=1000000, setup="from fib_py_double import fib_py_double")
print(f'Pure python (double): answer = {fib_py_double(n)}, time = {t}, speedup = {t1 / t}')

t = timeit.timeit(f"fib_py_cy_double({n})", number=1000000, setup="from fib_py_cy_double import fib_py_cy_double")
print(f'Pure python (double): answer = {fib_py_cy_double(n)}, time = {t}, speedup = {t1 / t}')

t = timeit.timeit(f"fib_cy_double({n})", number=1000000, setup="from fib_cy_double import fib_cy_double")
print(f'Pure python (double): answer = {fib_cy_double(n)}, time = {t}, speedup = {t1 / t}')
