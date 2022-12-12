class TV:
  is_on = False
  channel_no = 1

  def turn_on(self):
    self.is_on = True

  def turn_off(self):
    self.is_on = False

  def set_channel(self, new_channel_no):
    self.channel_no = new_channel_no

  def show_status(self):
    print(f"TV is {f'on, channel {self.channel_no}' if self.is_on else 'off'}")

tv = TV()

tv.show_status()

tv.turn_on()

tv.show_status()

tv.set_channel(5)

tv.show_status()

tv.turn_off()

tv.show_status()