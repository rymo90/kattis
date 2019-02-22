import math 
a,b,c,d = map(int,input().split())
svar= 0
if a ==b and a== c and a==d:
  svar= a*b
else:
  s = (a+b+c+d)/2
  svar= math.sqrt((s-a)*(s-b)*(s-c)*(s-d))

print(svar)
