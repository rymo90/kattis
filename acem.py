import sys
count = 0
time = 0
lis = dict()
while True:
    x = input().split()
    if x[0] == "-1":
        print(count, time)
        break

    else:
        lis[x[1]] = 0
        if x[2] == "right":
            count += 1
            print(lis)
            time += int(x[0])+lis[x[1]]*20
        else:
            lis[x[1]] += 1
