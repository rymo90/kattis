n = int(input())
for _ in range(n):
    g = list(map(int, input().split()))
    orginal = g
    g= g[1:]
    g= g[:-1]
    test= g[0]
    g= g[1:]
    if min(g) > test:
        print(g.index(max(g))+2)
    else:
        print(g.index(min(g))+2)
