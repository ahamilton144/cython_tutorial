# cython: profile=True

### main file to run simulation

import numpy as np
import pandas as pd
from Model cimport Model
from mpi4py import MPI

cdef class reservoir_sim():
  cdef public Model model

  def __init__(self, int years, bint plot, int seed):
    ### get MPI rank
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    ### initialize model
    self.model = Model(years = years, plot = plot, seed = rank)

    ### run simulation
    results = np.asarray(self.model.run()).transpose()
    results_df = pd.DataFrame(results, columns = ['r1_inflow', 'r1_upstream_release', 'r1_min_flow', 'r1_demand', 'r1_release', 'r1_delivery', 'r1_storage',
                                                  'r2_inflow', 'r2_upstream_release', 'r2_min_flow', 'r2_demand', 'r2_release', 'r2_delivery', 'r2_storage'])
    results_df.to_csv(f'results/seed{rank}.csv', index=False)

    ### plot results
    if self.model.plot:
      self.model.plot_results()

