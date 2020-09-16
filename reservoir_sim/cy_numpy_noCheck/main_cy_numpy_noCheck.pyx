# cython: profile=True

### main file to run simulation

from Model cimport Model

cdef class main_cy_numpy_noCheck():
  cdef public Model model

  def __init__(self, int years, bint plot, int seed):
    # initialize model
    self.model = Model(years = years, plot = plot, seed = seed)

    # run simulation
    self.model.tot_storage = self.model.run()

    # plot results
    if self.model.plot:
      self.model.plot_results()

