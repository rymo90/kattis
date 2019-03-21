import math
while True:
    num = sorted(list(map(int,input().split())))
    a = num[0]
    b= num[1]
    c = num[2]
    if a== 0 and b == 0 and c == 0:
        break
    else:
        if (math.sqrt(a*a+b*b)) == c:
            print("right")
        else:
            print("wrong")
