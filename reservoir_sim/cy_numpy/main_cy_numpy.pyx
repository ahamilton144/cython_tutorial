### main file to run simulation

from Model cimport Model

cdef class main_cy_numpy():
  cdef public Model model

  def __init__(self):
    # initialize model
    model = Model()

    # run simulation
    model.run_sim()

    # plot results
    model.plot_results()

