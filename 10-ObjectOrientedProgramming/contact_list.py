from contact import Contact

class ContactList:
  def __init__(self) -> None:
    self.contacts = []

  def add(self, contact: Contact):
    self.contacts.append(contact)

  def display(self):
    [print(i.get()) for i in self.contacts]