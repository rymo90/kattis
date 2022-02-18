n,m= map(int, input().split())
group = input().split()
count = 0
for i in range(len(group)):
    tt = int(group[i])
    if count + tt  > n:
        break
    else:
        count += tt

    m-=1
print(m)
