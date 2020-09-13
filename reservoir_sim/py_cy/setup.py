from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(['Model.py', 'Reservoir.py', 'Demand.py'],
                                annotate=True, language_level=3))
