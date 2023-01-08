class Account:
  def __init__(self, number: str) -> None:
    self.balance = 0
    self.number = number

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient funds on the account")

  def status(self):
    print(f"Bank account No: {self.number}")
    print(f"Balance: PLN {self.balance:.2f}")

acc = Account("12 3456 5555 9090 1111 0000 7722")

acc.status()

acc.deposit(25.30)

acc.status()

acc.withdraw(31.70)

acc.status()

acc.withdraw(14)

acc.status()