import statistics

class Statistics:
  def __init__(self) -> None:
    self.numbers = set()

  def add(self, number):
    self.numbers.add(number)

  def display(self):
    print(", ".join([str(i) for i in self.numbers]))

  def max(self):
    return max(self.numbers)

  def min(self):
    return min(self.numbers)

  def mean(self):
    return statistics.mean(self.numbers)

  def median(self):
    return statistics.median(self.numbers)

  def displayStats(self):
    print(f"min: {self.min()}")
    print(f"max: {self.max()}")
    print(f"mean: {self.mean()}")
    print(f"median: {self.median()}")

stats = Statistics()

stats.add(12)
stats.add(37)
stats.add(6)
stats.add(9)
stats.add(17)

stats.display()

stats.displayStats()