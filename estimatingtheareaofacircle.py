import math
stop = False
while not stop:
    r, m, c = map(float, input().split())
    if r == 0 and m == 0 and c == 0:
        stop = True
    else:
        areaOne = math.pi * math.pow(r, 2)
        temp = (c / m)
        areaTwo = temp * math.pow(2 * r, 2)
        print(areaOne, areaTwo)
