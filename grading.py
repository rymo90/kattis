grade= input().split()
scor = input()
svar = ""
alfabet = ["A","B","C","D","E"]
for i in range(len(grade)):

    if int(scor) >= int(grade[i]):
        svar =alfabet[i]
        break
if svar == "":
    svar = "F"
print(svar)
