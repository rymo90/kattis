

while True:
    ch = input()
    if ch[0] == "0":
        break
    else:
        t, n = ch.split()
        index = 0
        step1 = ""
        step2 = ""
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
        step1 = n[::-1]
        for i in range(len(step1)):
            index = alpha.index(step1[i])
            step2 += alpha[(index+int(t)) % len(alpha)]
        print(step2)
