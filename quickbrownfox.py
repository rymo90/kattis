import re
n = int(input())
la="abcdefghijklmnopqrstuvwxyz"
for _ in range(n):
    x = input()
    reg = re.findall(r"[a-zA-Z]",x)
    reg = ("".join(reg)).lower()
    res = ""
    svar = ""
    for i in range(len(reg)):
        tst = reg[i]
        if tst in la:
            if tst in res:
                continue
            else:
                res += tst
    sort = "".join(sorted(res))
    for j in range(len(la)):
        if la[j] in sort:
            pass
        else:
            svar += la[j]
    if svar == "":
        print("pangram")
    else:
        print("missing",svar)
