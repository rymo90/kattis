n = input()
sw= False
lft = 0
rgt = 0
svar= ""
for i in range(len(n)):

    if n[i] == ")":
        sw = True
    if n[i] == "|" and sw == False:
        lft += 1
    if n[i]== "|" and sw == True:
        rgt += 1
    else:
        continue
if rgt == lft:
    svar = "correct"
else:
    svar= "fix"
print(svar)
