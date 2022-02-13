n = int(input())
i = 1
k= 0
sm = i
if n <= 9:
    k = 0
else:
    while sm <= n:
        i = i+2
        sm  += i*i
        k+= 1
print(k)
