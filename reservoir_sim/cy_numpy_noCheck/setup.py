from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(['main_cy_numpy_noCheck.pyx', 'Model.pyx', 'Reservoir.pyx', 'Demand.pyx'],
                                annotate=True, language_level=3))
