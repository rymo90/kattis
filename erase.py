n = int(input())
a = list(input())
b = list(input())
for _ in range(n):
    for i in range(len(a)):
        if a[i] == "0":
            a[i] = "1"
        else:
            a[i] = "0"
c = 0
for j in range(len(b)):
    if b[j] == a[j]:
        c+=1
if c == len(a):
    print("Deletion succeeded")
else:
    print("Deletion failed")
