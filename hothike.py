a = input()
sv1 = 0
sv2= 0
b = list(map(int, input().split()))
sm= 41
for i in range(len(b)-2):
    tst = max(b[i],b[i+2])
    if tst <= sm :
        sm = tst
        sv1 = i+1
        sv2 = tst
print(sv1,sv2)
