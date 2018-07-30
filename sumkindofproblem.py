
p = int(input())
for _ in range(p):
    k, n = [int(i) for i in input().split()]
    s1 = int((n*(n+1))/2)
    s2 = n*n
    s3 = (n*n) + n
    print(k, s1, s2, s3)
