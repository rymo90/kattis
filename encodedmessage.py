import math
n = int(input())
for i in range(n):
    msg = ""
    encMsg = list(input())
    prt = int(math.sqrt(len(encMsg)))
    count = prt
    while prt > 0:
        msg += "".join(encMsg[prt-1::prt])
        encMsg[prt-1::prt] = [""]*count
        encMsg = list("".join(encMsg))
        prt -= 1
    print(msg)
