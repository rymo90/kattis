import sys
count = 1
lines = sys.stdin.readlines()
for i in range(len(lines)):
    x = lines[i].replace("\n","")

    tm= sorted(list(map(int, x[1:].split())))
    print("Case",str(count)+":",tm[0],tm[-1],tm[-1]-tm[0])
    count +=1
