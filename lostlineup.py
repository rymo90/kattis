n = int(input())
d = list(map(int,input().split()))
lis = [1]
dict = {}
c = sorted(d)
for _ in range(len(d)):
    dict[d[_]] = _+2
for i in range(len(c)):
    lis.append(dict[c[i]])
print(*lis)
