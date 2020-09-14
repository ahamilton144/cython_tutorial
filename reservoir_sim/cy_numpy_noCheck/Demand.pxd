### header file, declaring all attributes of Demand class. No need to declare functions unless they are cdef functions.

cdef class Demand():

  cdef:
    public str name

    public double demand_amp, demand_phase, demand_shift, demand_noise, days_to_radians

  cdef double demand_t(self, double t)
  