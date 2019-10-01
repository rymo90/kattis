sv = ""
for i in range(5):
    kryp = input()
    for k in range(len(kryp)-2):
        if kryp[k]== "F" and kryp[k+1]== "B" and kryp[k+2] == "I":
            sv += str(i+1) + " "
if sv == "":
    sv = "HE GOT AWAY!"
print(sv)
