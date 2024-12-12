import math
r = int(input("please, input radius \n"))
p = round(2 * math.pi * r, 2)
s = round(math.pi * r**2, 2)
print(f"your P, S is: {p}, {s}")

x, y = 10, 55
print (x,y)
x, y = y, x
print (x,y)

g = float(9.81)
l = int(input("please, input length \n"))
t = int(2) * math.pi * math.sqrt(l/g)
print(f"your period is : {t}")
