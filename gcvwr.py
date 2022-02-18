g,t,_ = map(int,input().split())
svar = g-t
l = input().split()
svar -= svar*0.10
tmp = 0
for _ in range(len(l)):
    svar -= int(l[_])
print(round(svar))
