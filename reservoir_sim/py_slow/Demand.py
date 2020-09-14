### Demand class - pure Python
import numpy as np

class Demand():
  def __init__(self, name, demand_params):
    self.name = name
    # amplitude, phase, shift, & noise std for sine wave of demands
    self.demand_amp, self.demand_phase, self.demand_shift, self.demand_noise = demand_params

  ### demand function
  def demand_t(self, t):
    noise = np.random.normal(0., self.demand_noise, 1)[0]
    demand_t = self.demand_amp * np.sin((t - self.demand_phase)  * 2. * np.pi / 365.) + self.demand_shift + noise
    return demand_t

