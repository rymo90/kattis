from itertools import permutations
a = str(input())
b= list(a)
comb = permutations(b, len(b))
lis = []
svar =""
for i in list(comb):
    tst = "".join(i)
    if tst not in lis:
        lis.append(tst)
lis = sorted(lis)
for j in range(len(lis)-1):
    if lis[j] == a:
        svar = lis[j+1]
if svar == "":
    print(0)
else:
    print(int(svar))
