import timeit
import sys

# get number of years from command line
years = int(sys.argv[1])
trials = int(sys.argv[2])
repeat = int(sys.argv[3])
version = sys.argv[4]
print(years, trials, repeat, version)

if version in ['py_slow', 'py_fast', 'py_cy', 'py_numpy', 'py_numpy_reservoir']:
  from Model import Model
  model = Model(years = years, plot = False, seed = 101)
  tot_storage = model.run()
  t1 = min(timeit.repeat(f"model = Model(years = {years}, plot = False, seed = 101); tot_storage = model.run()", number=trials, repeat=repeat, setup="from Model import Model; gc.enable()"))

elif version in ['cy', 'cy_numpy', 'cy_numpy_reservoir', 'cy_numpy_noCheck']:
  from main import main
  main_obj = main(years = years, plot = False, seed = 101)
  tot_storage = main_obj.model.tot_storage
  t1 = min(timeit.repeat(f"main_obj = main(years = {years}, plot = False, seed = 101); tot_storage = main_obj.model.tot_storage", number=trials, repeat=repeat, setup=f"from main import main; gc.enable()"))

if version == 'py_slow':
  print(f'{version}: answer = {tot_storage}, time = {t1}, efficiency  = {1.0}')
  with open('py_slow_time.txt', 'w') as f:
    f.write(str(t1))
elif version == 'py_fast':
  with open('py_fast_time.txt', 'w') as f:
    f.write(str(t1))
  with open('..//py_slow/py_slow_time.txt', 'r') as f:
    base_time = f.read()
    base_time = float(base_time)
  print(f'{version}: answer = {tot_storage}, time = {t1}, efficiency relative to py_slow = {base_time / t1}')
else:
  with open('../py_fast/py_fast_time.txt', 'r') as f:
    base_time = f.read()
    base_time = float(base_time)
  print(f'{version}: answer = {tot_storage}, time = {t1}, efficiency relative to py_fast = {base_time / t1}')

