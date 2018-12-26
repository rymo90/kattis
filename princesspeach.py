n,y = map(int, input().split())
lis= []
for _ in range(y):
    k = int(input())
    lis.append(k)
lis = sorted(lis)

counter = 0
for i in range(n):
    if i in lis:
        continue
    else:
        counter +=1
        print(i)
# print(counter, "counter")
# print(n, "original")
diff= abs(n-counter)
# print(abs(n-counter), "diff")
print("Mario got "+ str(diff)+" of the dangerous obstacles.")
