import math
n = int(input())
alpha = list("ABCDEFGHIJKLMNOPQRSTUWVXYZ '")
start = (2*math.pi*30)//len(alpha)
for _ in range(n):
    x = input()
    feet = 15
    for j in range(len(x)-1):
        letter = x[j]
        index = alpha.index(letter)
        nextletter = x[j+1]
        nextidex = alpha.index(nextletter)
        if index > nextidex:
            print(letter, index, nextletter, nextidex,
                  "left", index-nextidex)
        else:
            print(letter, index, nextletter, nextidex,
                  "right", index-nextidex)
    break
