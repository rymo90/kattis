

import math
INDEX = {c: i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ '")}
CIRCUM = math.pi*60
SPEED = 15


def circle_distance(a, b):
    d = min(abs(INDEX[a]-INDEX[b]),
            len(INDEX) - abs(INDEX[a]-INDEX[b]))
    return CIRCUM*(d/len(INDEX))


n = int(input())

for _ in range(n):
    s = input()
    time = len(s)
    for a, b in zip(s, s[1:]):
        time += circle_distance(a, b)/SPEED
    print(time)
