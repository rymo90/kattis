a = input()
svar = []
for i in range(len(a)-1):
    if a[i]== ":":
        if a[i+1] == ")":
            svar.append(i)
        elif a[i+1] == "-":
            if a[i+2] == ")":
                svar.append(i)

    elif  a[i] == ";":
        if a[i+1] == ")":
            svar.append(i)

        elif a[i+1] == "-":
            if a[i+2] == ")":
                svar.append(i)

for j in range(len(svar)):
    print(int(svar[j]))
