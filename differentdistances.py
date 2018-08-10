import math
while True:
    data= input()
    if data == "0":
        break
    else:
        x1,y1,x2,y2,p = [float(i) for i in data.split()]
        X = math.pow(abs(x1-x2),p)
        Y= math.pow(abs(y1-y2),p)
        XY= X+Y
        pNorm= math.pow(XY,1/p)
        print(pNorm)
