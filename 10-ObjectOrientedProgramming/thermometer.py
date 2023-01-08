import random

class Thermometer:

  max_temp = 42.0
  min_temp = 34.0

  def __init__(self):
    self.temperature = None
    self.turnedOn = False

  def turnOn(self):
    self.turnedOn = True

  def turnOff(self):
    self.turnedOn = False
  
  def measure(self):
    self.temperature = random.random() * (self.max_temp - self.min_temp) + self.min_temp

  def status(self):
    fever_msg = ""

    if self.temperature >= 37:
      fever_msg = "fever"
    
    if self.temperature >= 41:
      fever_msg = "CRITICAL TEMPERATURE!!!"

    print(f"Temperature: {self.temperature:4.2f} {fever_msg}")