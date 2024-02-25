import time
import os
import sys
import ST7735

from enviroplus import gas
from subprocess import PIPE, Popen



# Create ST7735 LCD display class
st7735 = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Initialize display
st7735.begin()

class Temp:
    def __init__(self):
        # Tuning factor for compensation. Decrease this number to adjust the
        # temperature down, and increase to adjust up
        self.factor = 2.25
        self.cpu_temps = [self.get_cpu_temperature()] * 5
        self.bme280 = BME280()
        
# Get the temperature of the CPU for compensation
    def get_cpu_temperature(self):
        process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
        output, _error = process.communicate()
        return float(output[output.index('=') + 1:output.rindex("'")])

    def get_temp(self):
      cpu_temp = self.get_cpu_temperature()
      # Smooth out with some averaging to decrease jitter
      self.cpu_temps = self.cpu_temps[1:] + [cpu_temp]
      avg_cpu_temp = sum(self.cpu_temps) / float(len(self.cpu_temps))
      raw_temp = self.bme280.get_temperature()
      return raw_temp - ((avg_cpu_temp - raw_temp) / self.factor)


def get_humidity():
  return bme280.get_humidity()

def get_pressure():
  return bme280.get_pressure()  

def get_light():
  return ltr559.get_lux()
