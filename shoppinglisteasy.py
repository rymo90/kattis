n,m = map(int,input().split())
dict = {}
for _ in range(n):
    a = input().split()
    for i in range(m):
        if a[i] in dict:
            dict[a[i]] += 1
        else:
            dict[a[i]]= 0
list = []
for key in dict:
    if dict[key] == n-1:
        list.append(key)
print(len(list))
list= sorted(list)
for _ in range(len(list)):
    print(list[_])
