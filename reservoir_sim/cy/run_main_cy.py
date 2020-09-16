### Need new main file so we can run the cythonized old main file (.pyx)

from main_cy import main_cy

main_cy(years = 5, plot = True, seed = 101)
