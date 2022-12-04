import re

def f(first_letter, last_letter):
  with open("test.txt") as file:
    data = file.read()

  pattern = f"\\b{first_letter}\\w*{last_letter}\\b"
  
  finds = re.findall(pattern, data)
  return len(finds)
