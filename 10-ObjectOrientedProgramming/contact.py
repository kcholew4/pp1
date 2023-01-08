class Contact:
  def __init__(self, name, email, telephone) -> None:
    self.name = name
    self.email = email
    self.telephone = telephone

  def get(self):
    return f"{self.name}, {self.email}, {self.telephone}"