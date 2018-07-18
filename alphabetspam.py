import math
s = input()
ws = 0
lc = 0
uc= 0
sl= 0
tot= len(s)
for i in s:
    if i.isupper():
        uc += 1
    elif i.islower():
        lc += 1
    elif i =="_" :
        ws += 1
    else:
        sl += 1
print(ws/tot)
print(lc/tot)
print(uc/tot)
print(sl/tot)
