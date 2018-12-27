a = list(map(int, input().split()))
b= input()
a= sorted(a)
lis= []
for i in range(len(b)):
    if b[i] == "A":
        lis.append(a[0])
    elif b[i] =="B":
        lis.append(a[1])
    else:
        lis.append(a[2])
print(*lis)
