a = int(input())
sum = 0
lis= []
k= 3
for i in range(a):
    x = int(input())
    lis.append(x)
lis.sort(reverse = True)

for j in range(len(lis)):
    if j+1 == k:
        k+=3
    else:
        sum+=lis[j]

print(sum)
