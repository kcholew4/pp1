alphabet = {
  "a": "Alfa",
  "b": "Bravo",
  "c": "Charlie",
  "d": "Delta",
  "e": "Echo",
  "f": "Foxtrot",
  "g": "Golf",
  "h": "Hotel",
  "i": "India",
  "j": "Juliet",
  "k": "Kilo",
  "l": "Lima",
  "m": "Mike",
  "n": "November",
  "o": "Oscar",
  "p": "Papa",
  "q": "Quebec",
  "r": "Romeo",
  "s": "Sierra",
  "t": "Tango",
  "u": "Uniform",
  "v": "Victor",
  "w": "Whiskey",
  "x": "xray",
  "y": "Yankee",
  "z": "Zulu"
}

text = input("Enter text (no numbers and special characters please): ")

spelledText = []

for char in text:
  spelledText.append(alphabet[char.lower()])

print(f"Spelled text: {' '.join(spelledText)}")