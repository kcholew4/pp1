file = open("shopping.txt", "a")

item = input("New item: ")

file.write(f"\n{item}")

file.close()