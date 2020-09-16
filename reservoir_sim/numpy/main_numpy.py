### main file to run simulation

from Model import Model

# initialize model
model = Model(years = 5, plot = False, seed = 101)

# run simulation
tot_storage = model.run()
print(tot_storage)

# plot results
if model.plot:
  model.plot_results()

