### Model class for running simulation
import matplotlib.pyplot as plt
import random
import numpy as np
from Reservoir import Reservoir

class Model():
  def __init__(self, years, plot, seed):
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
    self.reservoir_list = [self.reservoir_upper, self.reservoir_lower]
    self.output = {}
    for reservoir in self.reservoir_list:
      self.output[reservoir.name] = {}
      self.output[reservoir.name]['inflow'] = []
      self.output[reservoir.name]['upstream_release'] = []
      self.output[reservoir.name]['min_flow'] = []
      self.output[reservoir.name]['demand'] = []
      self.output[reservoir.name]['release'] = []
      self.output[reservoir.name]['delivery'] = []
      self.output[reservoir.name]['storage'] = [reservoir.storage]

  def run(self):
    for t in range(self.days):
      # step upper
      (inflow, upstream_release, min_flow, demand, release, delivery, storage) = self.reservoir_upper.step(t, 0.)
      self.output['upper']['inflow'].append(inflow)
      self.output['upper']['upstream_release'].append(upstream_release)
      self.output['upper']['min_flow'].append(min_flow)
      self.output['upper']['demand'].append(demand)
      self.output['upper']['release'].append(release)
      self.output['upper']['delivery'].append(delivery)
      self.output['upper']['storage'].append(storage)

      (inflow, upstream_release, min_flow, demand, release, delivery, storage) = self.reservoir_lower.step(t, release)
      self.output['lower']['inflow'].append(inflow)
      self.output['lower']['upstream_release'].append(upstream_release)
      self.output['lower']['min_flow'].append(min_flow)
      self.output['lower']['demand'].append(demand)
      self.output['lower']['release'].append(release)
      self.output['lower']['delivery'].append(delivery)
      self.output['lower']['storage'].append(storage)

    # return total storage last time step to make sure versions are equivalent
    return self.output['upper']['storage'][-1] + self.output['lower']['storage'][-1]

  def plot_results(self):
    t = np.arange(self.days)
    t_storage = np.arange(-1, self.days)

    fig, ((ax11, ax12, ax13, ax14), (ax21, ax22, ax23, ax24)) = plt.subplots(2, 4, figsize=(12,6))
    # make a little extra space between the subplots
    fig.subplots_adjust(hspace=0.5)
    ax11.plot(t, self.output['upper']['inflow'], c='indianred')
    ax11.plot(t, np.array(self.output['upper']['inflow']) + np.array(self.output['upper']['upstream_release']), c='k')
    ax11.legend(['Inflow', 'w/ UpRel'])
    ax12.plot(t, self.output['upper']['demand'], c='indianred')
    ax12.plot(t, self.output['upper']['delivery'], c='k')
    ax12.legend(['Demand', 'Deliv'])
    ax13.plot(t, self.output['upper']['min_flow'], c='indianred')
    ax13.plot(t, self.output['upper']['release'], c='k')
    ax13.legend(['MinFl', 'Release'])
    ax14.plot(t_storage, self.output['upper']['storage'], c='k')
    ax14.legend(['Storage'])

    ax21.plot(t, self.output['lower']['inflow'], c='indianred')
    ax21.plot(t, np.array(self.output['lower']['inflow']) + np.array(self.output['lower']['upstream_release']), c='k')
    ax21.legend(['Inflow', 'w/ UpRel'])
    ax22.plot(t, self.output['lower']['demand'], c='indianred')
    ax22.plot(t, self.output['lower']['delivery'], c='k')
    ax22.legend(['Demand', 'Deliv'])
    ax23.plot(t, self.output['lower']['min_flow'], c='indianred')
    ax23.plot(t, self.output['lower']['release'], c='k')
    ax23.legend(['MinFl', 'Release'])
    ax24.plot(t_storage, self.output['lower']['storage'], c='k')
    ax24.legend(['Storage'])

    plt.show()



