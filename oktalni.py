x = list(input())
x.reverse()
sm= 0
for i in range(len(x)):
    sm+=int(x[i])*2**i
# while sm >= 0:
sv= ""
while sm >0:
    sv += str(sm%8)
    sm = sm// 8
print(int(sv[::-1]))
