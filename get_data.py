import time
import os
import sys
import ST7735
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280
from enviroplus import gas
from subprocess import PIPE, Popen

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

cpu_temps = [get_cpu_temperature()] * 5

def get_temp():
  cpu_temp = get_cpu_temperature()
  # Smooth out with some averaging to decrease jitter
  cpu_temps = cpu_temps[1:] + [cpu_temp]
  avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
  raw_temp = bme280.get_temperature()
  return raw_temp - ((avg_cpu_temp - raw_temp) / factor)

def get_humidity():
  return bme280.get_humidity()

def get_pressure():
  return bme280.get_pressure()  

def get_light():
  return ltr559.get_lux()
