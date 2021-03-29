n = int(input())
tmp = []
while n > 0:
    t = input()
    tmp.append(t)
    n -=1

counter = len(tmp)-1
while counter >= 0:
    print(int(tmp[counter]))
    counter -=1
