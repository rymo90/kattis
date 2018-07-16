import math
number = int(input())
while number > 0:
    data = input().split()
    volecity=data[0]
    degree=data[1]
    distance= data[2]
    hight1= data[3]
    hight2 = data[4]
    vox=float(volecity)*math.cos(math.radians(float(degree)))
    voy = float(volecity)*math.sin(math.radians(float(degree)))
    time= (float(distance))/vox
    gforce= 9.81
    yWall= (voy*float(time)-((1/2)*gforce*math.pow(float(time),2)))
    min= float(eval(hight1)) + 1
    max= float(eval(hight2))-1
    if yWall >= min and yWall <= max:
        print("Safe")
    else:
        print("Not Safe")
    number -= 1
