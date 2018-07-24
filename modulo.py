lis = []
count = 0
for i in range(10):
    x = int(input())
    ck = x % 42
    if ck in lis:
        pass
    else:
        count += 1
        lis.append(ck)
print(count)
