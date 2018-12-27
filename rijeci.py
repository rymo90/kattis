x = int(input())
a = 0
b = 1
for i in range(x):
    prev = a
    if i == 0:
        pass
    else:
        a= b
        b = prev+b
print(a,b)
