import re

text = "To be, or not to be, that is the question"

vowels = re.findall(r"[aeiouy]", text)

print(len(vowels))