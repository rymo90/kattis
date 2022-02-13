s = input()
k  = []
svar = 1
for i in range(len(s)):
    if s[i] in k :
        svar= 0
        break
    else:
        k.append(s[i])
print(svar)
