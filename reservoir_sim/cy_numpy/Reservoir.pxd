### header file, declaring all attributes of Reservoir class. No need to declare functions unless they are cdef functions.

from Demand cimport Demand

cdef class Reservoir():

  cdef:
    public str name

    public double inflow_amp, inflow_phase, inflow_shift, inflow_noise, min_flow_amp, min_flow_phase, min_flow_shift, capacity, storage, days_to_radians

    public Demand demand

  cdef double inflow_t(self, double t)

  cdef double min_flow_t(self, double t)

  cdef (double, double, double, double, double, double, double) step(self, double t, double upstream_release)
  