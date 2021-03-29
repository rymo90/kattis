g = input()
num = 0
s= "e"
for _ in range(len(g)):
    if g[_] == "e":
        num += 1
sv = "".join([char*(num*2) for char in s])
print("h"+sv+"y")
