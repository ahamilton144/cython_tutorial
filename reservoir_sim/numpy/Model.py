### Model class for running simulation
import matplotlib.pyplot as plt
import numpy as np
from Reservoir import Reservoir

class Model():
  def __init__(self):
    self.years = 5
    self.days = 365 * self.years
    # self.step_output_per_reservoir = 7

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
    self.reservoir_list = [self.reservoir_lower, self.reservoir_upper]
    self.num_reservoirs = len(self.reservoir_list)

    self.num_step_outputs = 7
    
    self.output = np.zeros((self.num_reservoirs * self.num_step_outputs, self.days + 1))
    for i, reservoir in enumerate(self.reservoir_list):
      self.output[i * self.num_step_outputs + self.num_step_outputs - 1, 0] = reservoir.storage

  def run(self):
    for t in range(1, self.days + 1):
      # step upper
      (inflow, upstream_release, min_flow, demand, release, delivery, storage) = self.reservoir_upper.step(t, 0.)
      self.output[0, t] = inflow
      self.output[1, t] = upstream_release
      self.output[2, t] = min_flow
      self.output[3, t] = demand
      self.output[4, t] = release
      self.output[5, t] = delivery
      self.output[6, t] = storage

      (inflow, upstream_release, min_flow, demand, release, delivery, storage) = self.reservoir_lower.step(t, release)
      self.output[self.num_step_outputs, t] = inflow
      self.output[self.num_step_outputs + 1, t] = upstream_release
      self.output[self.num_step_outputs + 2, t] = min_flow
      self.output[self.num_step_outputs + 3, t] = demand
      self.output[self.num_step_outputs + 4, t] = release
      self.output[self.num_step_outputs + 5, t] = delivery
      self.output[self.num_step_outputs + 6, t] = storage

  def plot_results(self):
    t = np.arange(self.days + 1)

    fig, ((ax11, ax12, ax13, ax14), (ax21, ax22, ax23, ax24)) = plt.subplots(2, 4, figsize=(12,6))
    # make a little extra space between the subplots
    fig.subplots_adjust(hspace=0.5)
    ax11.plot(t, self.output[0, :], c='indianred')
    ax11.plot(t, self.output[0, :] + self.output[1, :], c='k')
    ax11.legend(['Inflow', 'w/ UpRel'])
    ax12.plot(t, self.output[3, :], c='indianred')
    ax12.plot(t, self.output[5, :], c='k')
    ax12.legend(['Demand', 'Deliv'])
    ax13.plot(t, self.output[2, :], c='indianred')
    ax13.plot(t, self.output[4, :], c='k')
    ax13.legend(['MinFl', 'Release'])
    ax14.plot(t, self.output[6, :], c='k')
    ax14.legend(['Storage'])

    ax21.plot(t, self.output[self.num_step_outputs + 0, :], c='indianred')
    ax21.plot(t, self.output[self.num_step_outputs + 0, :] + self.output[self.num_step_outputs + 1, :], c='k')
    ax21.legend(['Inflow', 'w/ UpRel'])
    ax22.plot(t, self.output[self.num_step_outputs + 3, :], c='indianred')
    ax22.plot(t, self.output[self.num_step_outputs + 5, :], c='k')
    ax22.legend(['Demand', 'Deliv'])
    ax23.plot(t, self.output[self.num_step_outputs + 2, :], c='indianred')
    ax23.plot(t, self.output[self.num_step_outputs + 4, :], c='k')
    ax23.legend(['MinFl', 'Release'])
    ax24.plot(t, self.output[self.num_step_outputs + 6, :], c='k')
    ax24.legend(['Storage'])

    plt.show()



