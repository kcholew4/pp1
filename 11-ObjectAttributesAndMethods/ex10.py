class Phone:

  def __init__(self, roaming, carrier) -> None:
    self.on = False
    self.roaming = roaming
    self.carrier = carrier

  def togglePowerButton(self):
    self.on = not self.on
  
  def changeCarrier(self, name):
    self.carrier = name

  def __str__(self):
    return f"Phone is {'on' if self.on else 'off'}, roaming: {'active' if self.roaming else 'not active'}, carrier: {self.carrier}"

phone1 = Phone(False, "orange")

phone1.togglePowerButton()
phone1.changeCarrier("play")

print(phone1)

phone2 = Phone(True, "t-mobile")

phone2.togglePowerButton()
phone2.changeCarrier("plus")

print(phone2)