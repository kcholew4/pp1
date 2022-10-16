a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side a: "))

s = (a + b + c) / 2;

area = (s * (s - a) * (s - b) * (s - c))**(1/2)

print("Area {}".format(area))