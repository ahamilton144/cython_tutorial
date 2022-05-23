#!/usr/bin/env python3

### Need new main file so we can run the cythonized old main file (.pyx)

from reservoir_sim import reservoir_sim

reservoir_sim(years = 5, plot = False, seed = 101)
