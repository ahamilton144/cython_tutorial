### header file, declaring all attributes of Model class. No need to declare functions unless they are cdef functions.

from Reservoir cimport Reservoir

cdef class Model():

  cdef:
    public int years, days, num_step_outputs

    public double tot_storage

    public double[:,:] output

    public bint plot

    public Reservoir reservoir_upper, reservoir_lower
  
  cdef double run(self)
  