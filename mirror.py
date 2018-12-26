t = int(input())
count= 1
for _ in range(t):
    r, c = map(int, input().split())
    lis= []
    for d in range(r):
        l = input().split()
        lis.append(l)

    lis = list(reversed(lis))
    print("Test", count)
    for i in range(len(lis)):
        ts= "".join(lis[i])
        if '*' in ts:
            print("".join(list(reversed(ts))))
        else:
            print(ts)
    count+=1
