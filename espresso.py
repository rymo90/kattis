x, s = map(int,input().split())
svar= 0
num = 0
lst= 0
for i in range(x):
    n = input()
    lst = int(n[0])
    if len(n) > 1:
        lst += 1

    if lst - s == 0:
        svar += 0
        s

print(svar)
