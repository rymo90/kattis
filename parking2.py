t = int(input())
for i in range(t):
    n = input()
    sum = 0
    x = sorted([int(j) for j in input().split()])
    for i in range(len(x) - 1):
        sum += x[i + 1] - x[i]
    print(sum * 2)
