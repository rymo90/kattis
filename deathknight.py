import re
n = int(input())
count = 0
for i in range(n):
    won = True
    s = list(input())
    for j in range(len(s)-1):
        if s[j] == "C" and s[j+1] == "D":
            won = False
    if won == True:
        count += 1
print(count)
