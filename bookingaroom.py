r, n = map(int, input().split())
found = True
lis= []
if r == n:
    print("too late")
else:
    for _ in range(n):
        x= int(input())
        if x <= r and x >=1:
            lis.append(x)
    lis  = sorted(lis)
    for i in range(r):
        if i+1 in lis:
            continue
        else:
            print(i+1)
            break    
