

import math
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
circle = (math.pi*60)

n = int(input())
for _ in range(n):
    s = input()
    time = len(alpha)

    for i in range(len(s)-1):
        index = alpha.index(s[i])
        nextIndex = alpha.index(s[i+1])
        distance = min(abs(index-nextIndex), len(alpha)-abs(index-nextIndex))

        time += circle*(distance/len(alpha))/15
    print(time)
