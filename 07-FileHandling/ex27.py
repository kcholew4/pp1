import re
import statistics

with open("grades.txt") as file:
  content = file.read()

grades = [float(i) for i in re.findall(r"\d\.\d", content)]

print(statistics.mean(grades))