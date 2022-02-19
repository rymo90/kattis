a = input()
cpr= "432765-4321"
sumVal = 0
for i in range(len(a)):
    if a[i] == "-":
        continue
    else:
        sumVal += int(a[i]) * int(cpr[i])

if sumVal%11 == 0:
    print(1)
else:
    print(0)
