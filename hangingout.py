l, x = [int(i) for i in input().split()]
count = 0
current = 0
for j in range(x):
    p = input().split()
    if p[0] == "enter":
        if int(p[1]) + current <= l:
            current += int(p[1])
        else:
            count += 1
    else:
        current -= int(p[1])
print(count)
