class TV:

  def __init__(self):
    self.is_on = False
    self.channel_no = 1
    self.volume = 0

  def increase_volume(self):
    if self.volume == 10:
      return
    
    self.volume += 1

  def decrease_volume(self):
    if self.volume == 0:
      return

    self.volume -= 1

  def turn_on(self):
    self.is_on = True

  def turn_off(self):
    self.is_on = False

  def set_channel(self, new_channel_no):
    self.channel_no = new_channel_no

  def show_status(self):
    on_status = f'channel: {self.channel_no}, volume: {self.volume}'

    print(f"TV is {f'on, {on_status}' if self.is_on else 'off'}")

tv = TV()

tv.show_status()

tv.turn_on()

tv.increase_volume()
tv.increase_volume()
tv.increase_volume()

tv.show_status()

tv.set_channel(5)

tv.decrease_volume()

tv.show_status()

tv.turn_off()

tv.show_status()