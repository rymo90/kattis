han = input()
perm = input()
count = 10
lenhan = len(han)
for i in range(len(perm)):
    found = False
    ck = perm[i]
    for j in range(len(han)):
            if ck == han[j]:
                lenhan -= 1
                found = True
    if not found:
        count -= 1
    if lenhan == 0:
        print("WIN")
        break
    if count == 0:
        print("LOSE")
        break
