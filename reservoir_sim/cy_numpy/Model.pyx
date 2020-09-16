# cython: profile=True

### Model class for running simulation
import matplotlib.pyplot as plt
import numpy as np
import random
from Reservoir cimport Reservoir

cdef class Model():
  def __init__(self, int years, bint plot, int seed):
    cdef int i

    # length of simulation (no leap years)
    self.years = years
    self.days = 365 * self.years
    # boolean for whether to plot
    self.plot = plot
    # random seed
    random.seed(seed)


    ### set up upper reservoir
    # inflow params in terms of sinusoid, (amplitude, phase, shift, noise). units = AF/day
    inflow_params = (300., 0., 500., 20.)
    # min flow params in terms of sinusoid, (amplitude, phase, shift). units = AF/day
    min_flow_params = (200., 122., 300.)
    # demand params in terms of sinusoid, (amplitude, phase, shift, noise). units = AF/day
    demand_params = (300., 163., 600., 30.)
    # storage params (capacity, starting storage). units = AF
    storage_params = (500000., 250000.)
    # initialize upper reservoir
    self.reservoir_upper = Reservoir('upper', inflow_params, min_flow_params, demand_params, storage_params)

    ### set up lower reservoir
    # inflow params in terms of sinusoid, (amplitude, phase, shift, noise). units = AF/day
    inflow_params = (200., 30., 600., 100.)
    # min flow params in terms of sinusoid, (amplitude, phase, shift). units = AF/day
    min_flow_params = (100., 91., 400.)
    # demand params in terms of sinusoid, (amplitude, phase, shift, noise). units = AF/day
    demand_params = (100., 152., 300., 10.)
    # storage params (capacity, starting storage). units = AF
    storage_params = (20000., 15000.)
    # initialize lower reservoir
    self.reservoir_lower = Reservoir('lower', inflow_params, min_flow_params, demand_params, storage_params)

    ### set up data storage
    reservoir_list = [self.reservoir_upper, self.reservoir_lower]
    num_reservoirs = len(reservoir_list)
    self.num_step_outputs = 7
    
    output_np = np.zeros((num_reservoirs * self.num_step_outputs, self.days + 1))
    self.output = output_np

    for i in range(len(reservoir_list)):
      self.output[i * self.num_step_outputs + self.num_step_outputs - 1, 0] = reservoir_list[i].storage


  cdef double run(self):
    cdef int t
    cdef double inflow, upstream_release, min_flow, demand, release, delivery, storage
    for t in range(1, self.days + 1):
      t_run = float(t - 1)

      (inflow, upstream_release, min_flow, demand, release, delivery, storage) = self.reservoir_upper.step(t_run, 0.)
      self.output[0, t] = inflow
      self.output[1, t] = upstream_release
      self.output[2, t] = min_flow
      self.output[3, t] = demand
      self.output[4, t] = release
      self.output[5, t] = delivery
      self.output[6, t] = storage

      (inflow, upstream_release, min_flow, demand, release, delivery, storage) = self.reservoir_lower.step(t_run, release)
      self.output[7, t] = inflow
      self.output[8, t] = upstream_release
      self.output[9, t] = min_flow
      self.output[10, t] = demand
      self.output[11, t] = release
      self.output[12, t] = delivery
      self.output[13, t] = storage

    # return total storage last time step to make sure versions are equivalent
    return self.output[6, -1] + self.output[-1, -1]


  def plot_results(self):
    t = np.arange(self.days + 1)
    output = np.array(self.output)

    fig, ((ax11, ax12, ax13, ax14), (ax21, ax22, ax23, ax24)) = plt.subplots(2, 4, figsize=(12,6))
    # make a little extra space between the subplots
    fig.subplots_adjust(hspace=0.5)
    ax11.plot(t, output[:, 0], c='indianred')
    ax11.plot(t, output[:, 0] + output[:, 1], c='k')
    ax11.legend(['Inflow', 'w/ UpRel'])
    ax12.plot(t, output[:, 3], c='indianred')
    ax12.plot(t, output[:, 5], c='k')
    ax12.legend(['Demand', 'Deliv'])
    ax13.plot(t, output[:, 2], c='indianred')
    ax13.plot(t, output[:, 4], c='k')
    ax13.legend(['MinFl', 'Release'])
    ax14.plot(t, output[:, 6], c='k')
    ax14.legend(['Storage'])

    ax21.plot(t, output[:, self.num_step_outputs + 0], c='indianred')
    ax21.plot(t, output[:, self.num_step_outputs + 0] + output[:, self.num_step_outputs + 1], c='k')
    ax21.legend(['Inflow', 'w/ UpRel'])
    ax22.plot(t, output[:, self.num_step_outputs + 3], c='indianred')
    ax22.plot(t, output[:, self.num_step_outputs + 5], c='k')
    ax22.legend(['Demand', 'Deliv'])
    ax23.plot(t, output[:, self.num_step_outputs + 2], c='indianred')
    ax23.plot(t, output[:, self.num_step_outputs + 4], c='k')
    ax23.legend(['MinFl', 'Release'])
    ax24.plot(t, output[:, self.num_step_outputs + 6], c='k')
    ax24.legend(['Storage'])

    plt.show()


