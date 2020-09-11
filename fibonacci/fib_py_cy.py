### Function for finding n'th Fibonacci number. Copied from (Kurt W. Smith, "Cython", O'Reilly Media Inc., 2015).
### Pure Python version that we will cythonize

def fib_py_cy(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = a + b, a
    return a
