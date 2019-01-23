n = int(input())
for _ in range(n):
    lis = []
    c= list(map(int, input().split()))[1:]
    avg= sum(c)/len(c)
    for i in range(len(c)):
        if c[i] > avg:
            lis.append(c[i])
    ans= "{:.3f}".format((len(lis) / len(c))*100)+"%"
    print(ans)
