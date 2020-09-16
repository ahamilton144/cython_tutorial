### Need new main file so we can run the cythonized old main file (.pyx)

from main_cy_numpy import main_cy_numpy

main_cy_numpy(years = 5, plot = True, seed = 101)
