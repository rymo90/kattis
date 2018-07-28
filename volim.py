player = 0
stop = False
for i in range(n):
    t, z = [i for i in input().split()]
    holtid += int(t)
    if z == "T":
        if holtid < sec:
            if k < 8:
                k += 1
            else:
                k = 1
        else:
            player = k
    else:
        if holtid > sec:
            player = k
        else:
            continue
print(player)
