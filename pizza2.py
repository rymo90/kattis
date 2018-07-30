import math
r, c = [int(i) for i in input().split()]
pizza = math.pi*r**2
ost = math.pi*(r-c)**2
percent = (ost/pizza) * 100
print(percent)
