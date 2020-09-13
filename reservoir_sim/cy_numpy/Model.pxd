### header file, declaring all attributes of Model class. No need to declare functions unless they are cdef functions.

from Reservoir cimport Reservoir

cdef class Model():

  cdef:
    public int years, days, num_reservoirs, num_step_outputs

    public double[:, :] output

    public Reservoir reservoir_upper, reservoir_lower
  
  cdef void run_sim(self)
  