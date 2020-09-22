# Cython tutorial
This repository will serve as a brief introduction to Cython, for researchers interested in speeding up their Python models. 

I am still learning how to best use Cython myself, so I am not an expert. If you see anything wrong/suboptimal about what I'm doing, please let me know!

## Other resources
For more information, as always, see the [Cython docs](https://cython.readthedocs.io/en/latest/). 

I also highly recommend the book ["Cython", by Kurt W. Smith](https://www.oreilly.com/library/view/cython/9781491901731/) for more details and examples. It also looks like the author also has a [tutorial](https://github.com/kwmsmith/scipy-2017-cython-tutorial), but I haven't tried it yet.

Lastly, if you want to write more efficient pure Python prior to diving into Cython, ["High Performance Python" by Micha Gorelick and Ian Ozsvald](https://www.oreilly.com/library/view/high-performance-python/9781492055013/) is a good resource.

## Requirements
You will need a working Python 3 environment (preferably 3.6+ to avoid dependency issues) with NumPy, Cython, Matplotlib, and Jupyter.

You will also need the right compiler. OSX and Linux (including WSL) users should already have gcc standard. Windows users will need to download Microsoft Visual Studio 2019 to make sure you have the right compiler. Choose “Desktop development with C++” when it asks which programs you want to install.

## Jupyter tutorial
See the Jupyter notebook ``tutorial.ipynb`` for more details on the two examples below.

## Fibonacci example
The first example is a simple function that will calculate the n'th Fibonacci number. I have written six different versions of the function:

1. ``fib_py.py``: A pure Python implementation which counts using integers.
1. ``fib_py_cy.py``: The same implementation as #1, but we will Cythonize the Python code without making any changes.
1. ``fib_cy.pyx``: A typed Cythonic implementation.
1. ``fib_py_double.py``: Same as #1, but using doubles.
1. ``fib_py_cy_double.py``: Same as #2, but using doubles.
1. ``fib_cy_double.py``: Same as #3, but using doubles.

You can Cythonize files 2, 3, 5, & 6 using the command ``run_setups.sh python`` or ``run_setups.sh python3``, depending on the command for Python 3 in your terminal.

Then you can time all 6 versions using the command ``python time_versions.py`` (or ``python3``). Try changing ``n`` to a larger number, say 50, to see the important differences between the int and double versions.

## Reservoir simulation example
The reservoir simulation example is a more complex, object-oriented model. Although very simple compared to real water resources models, its structure still reduces the benefits of Cython when compared to the tight numerical loop of the Fibonacci example. It also requires us to learn about "Extension types", which are Cythonized, compiled classes.

I have written 7 different versions.

1. ``py_slow``: This was my first attempt at the simulation model, which is relatively slow due to the use of NumPy functions (random.normal, sin, pi) as opposed to the simpler versions in the ``random`` and ``math`` modules. I left this in to show that often the bottlenecks are simple things that can be fixed with purely Pythonic solutions - fixing these small things made a larger difference for this code than any Cythonization.
1. ``py_fast``: Pure Python version after switching modules as described above.
1. ``py_cy``: Same code as #2, but we will Cythonize the code without making any other changes.
1. ``numpy``: Same as #2, but using NumPy rather than dictionaries/lists for storing output data
1. ``cy``: (Mostly) typed Cythonic implementation.
1. ``cy_numpy``: Same as #5, but using NumPy plus memoryviews for storing output data.
1. ``cy_numpy_noCheck``: Same as #6, but with bounds checking and wraparounds disabled strategically.

You can Cythonize all relevant files and time all six versions using the command ``sh time_versions.sh python`` (or ``python3``). 
