import timeit
import sys

# get number of years from command line
years = int(sys.argv[1])
trials = int(sys.argv[2])
repeat = int(sys.argv[3])
version = sys.argv[4]
print(years, trials, repeat, version)

if version in ['py_slow', 'py_fast', 'py_cy', 'numpy']:
  from Model import Model
  model = Model(years = years, plot = False, seed = 101)
  tot_storage = model.run()
  t1 = min(timeit.repeat(f"model = Model(years = {years}, plot = False, seed = 101); tot_storage = model.run()", number=trials, repeat=repeat, setup="from Model import Model; gc.enable()"))

elif version in ['cy', 'cy_numpy', 'cy_numpy_noCheck']:
  if version == 'cy':
    from main_cy import main_cy as main
  elif version == 'cy_numpy':
    from main_cy_numpy import main_cy_numpy as main
  elif version == 'cy_numpy_noCheck':
    from main_cy_numpy_noCheck import main_cy_numpy_noCheck as main
  
  main_obj = main(years = years, plot = False, seed = 101)
  tot_storage = main_obj.model.tot_storage
  t1 = min(timeit.repeat(f"main_obj = main_{version}(years = {years}, plot = False, seed = 101); tot_storage = main_obj.model.tot_storage", number=trials, repeat=repeat, setup=f"from main_{version} import main_{version}; gc.enable()"))

if version == 'py_slow':
  print(f'{version}: answer = {tot_storage}, time = {t1}, speedup = {1.0}')
  with open('py_slow_time.txt', 'w') as f:
    f.write(str(t1))
elif version == 'py_fast':
  with open('py_fast_time.txt', 'w') as f:
    f.write(str(t1))
  with open('..//py_slow/py_slow_time.txt', 'r') as f:
    base_time = f.read()
    base_time = float(base_time)
  print(f'{version}: answer = {tot_storage}, time = {t1}, speedup over py_slow = {base_time / t1}')
else:
  with open('../py_fast/py_fast_time.txt', 'r') as f:
    base_time = f.read()
    base_time = float(base_time)
  print(f'{version}: answer = {tot_storage}, time = {t1}, speedup over py_fast = {base_time / t1}')

