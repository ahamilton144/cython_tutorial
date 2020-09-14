### Reservoir class - pure Python
import numpy as np
from Demand import Demand

class Reservoir():
  def __init__(self, name, inflow_params, min_flow_params, demand_params, storage_params):
    self.name = name
    # amplitude, phase, shift, & noise std for sine wave of inflows
    self.inflow_amp, self.inflow_phase, self.inflow_shift, self.inflow_noise = inflow_params
    # amplitude, phase, and shift for sine wave of minimum flows
    self.min_flow_amp, self.min_flow_phase, self.min_flow_shift = min_flow_params
    # reservoir capacity and initial storage
    self.capacity, self.storage = storage_params
    # set up demand object
    self.demand = Demand(name, demand_params)

  ### inflow function
  def inflow_t(self, t):
    noise = np.random.normal(0., self.inflow_noise, 1)[0]
    inflow_t = self.inflow_amp * np.sin((t - self.inflow_phase)  * 2. * np.pi / 365.) + self.inflow_shift + noise
    return inflow_t

  ### min flow function
  def min_flow_t(self, t):
    min_flow_t = self.min_flow_amp * np.sin((t - self.min_flow_phase)  * 2. * np.pi / 365.) + self.min_flow_shift
    return min_flow_t

  ### step reservoir another day
  def step(self, t, upstream_release):
    inflow = self.inflow_t(t)
    min_flow = self.min_flow_t(t)
    demand = self.demand.demand_t(t)
    
    # first assume release & delivery meet min_flow and demand exactly
    release = min_flow
    delivery = demand
    self.storage += inflow + upstream_release - release - demand

    # check if storage overflow
    if self.storage > self.capacity:
      release += self.storage - self.capacity
      self.storage = self.capacity

    # check if storage went negative. if so, curtail demand first, then env flows
    elif self.storage < 0:
      if delivery > (-self.storage):
        delivery += self.storage
        self.storage = 0.
      else:
        self.storage += delivery
        delivery = 0
        if release > (-self.storage):
          release += self.storage
          self.storage = 0
        else:
          print('This should not be happening')
    
    return (inflow, upstream_release, min_flow, demand, release, delivery, self.storage)
        


    