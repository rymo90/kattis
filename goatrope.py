
import math
x,y,x1,y1,x2,y2= map(int,input().split())
if x > x2:
  if y > y2:
    sv= (math.pow(x2-x,2)+math.pow(y-y2,2))
    print(math.sqrt(sv))
  elif y >= y1 and y <= y2:  
    print((abs(x-x2)))
  else:
    sv  = (math.pow(x2-x,2)+math.pow(y1-y,2))
    print(math.sqrt(sv))
elif x >=x1 and x <= x2:
  if y <= y1:
    print((abs(y-y1)))
  else :
    print((abs(y-y2)))
else:
  if y > y2:
    sv = (math.pow(x1-x,2)+math.pow(y-y2,2))
    print(math.sqrt(sv))
  elif y >= y1 and y <= y2:
    print((abs(x1-x)))
  else:
    sv= (math.pow(x-x1,2)+math.pow(y-y1,2))
    print(math.sqrt(sv)) 
