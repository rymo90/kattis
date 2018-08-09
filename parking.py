a, b, c = map(int, input().split())
dic = {}
dic[1] = a
dic[2] = b*2
dic[3] = c*3
print(dic)
fst = []
sec = []
for _ in range(3):
    temp1, temp2 = map(int, input().split())
    fst.append(temp1)
    sec.append(temp2)
print(min(fst), max(sec))
car = 0
cost = 0
previous =
for i in range(min(fst), max(sec)+1):
    if i in fst:
        cost += dic[i] * abs(previous-i)
        previous = i
        car += 1
    elif i in sec:
        print("out", i)
