n  = int(input())
for _ in range(n):
    lis = input().split()
    k = int(lis[0])
    lis = lis[1:]
    sum = 0
    for _ in range(k):
        sum+= int(lis[_])
    print(sum-(k-1))
