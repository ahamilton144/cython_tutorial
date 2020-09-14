### header file, declaring all attributes of Model class. No need to declare functions unless they are cdef functions.

from Reservoir cimport Reservoir

cdef class Model():

  cdef:
    public int years, days

    public double tot_storage

    public bint plot

    public list reservoir_list

    public dict output

    public Reservoir reservoir_upper, reservoir_lower
  
  cdef double run(self)
  