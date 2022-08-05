### Demand class - pure Python
from random import gauss
from math import pi, sin

class Demand():
  def __init__(self, name, demand_params):
    self.name = name
    # amplitude, phase, shift, & noise std for sine wave of demands
    self.demand_amp, self.demand_phase, self.demand_shift, self.demand_noise = demand_params
    # save 2pi/365 to save conversion time
    self.days_to_radians = 2. * pi / 365.

  ### demand function
  def demand_t(self, t):
    noise = gauss(0., self.demand_noise)
    demand_t = self.demand_amp * sin((t - self.demand_phase)  * self.days_to_radians) + self.demand_shift + noise
    return demand_t

