string = 'X-DSPAM-Confidence:0.8475'

pos = string.find(":")

num = float(string[pos + 1:])

print(num)