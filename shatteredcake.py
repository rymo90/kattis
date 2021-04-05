w = int(input())
n = int(input())
i= 0
res = 0
while i< n :
    a,b  = map(int,input().split())
    res += a*b
    i+=1
print(round(res/w))
