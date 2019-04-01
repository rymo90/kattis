input()
a = list(map(int,input().split()))
sm= 0
for i in range(len(a)):
    if a[i] < 0:
        sm += a[i]
print(sm*-1)
