import re
import statistics

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

temps = [int(i) for i in re.findall(r"\d{2}", message)]

print(statistics.mean(temps))