n , k = input().split()
k = int(k)
n = int(n)
i = 0
r = 0
mintal = 0
maxtal = 0
while i < k:
    r += int(input())
    i+=1
while k < n:
    mintal += -3
    maxtal += 3
    k+=1
print(float((mintal+r)/n), float((maxtal+r)/n) )
