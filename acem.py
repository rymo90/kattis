
count = 0
time = 0
lis = dict()
lista = []
while True:
    x = input().split()
    if x[0] == "-1":
        break
    else:
        lista.append(x)
        lis[x[1]] = 0
for i in range(len(lista)):
    if lista[i][2] == "right":
        count += 1
        time += int(lista[i][0])+(lis[lista[i][1]]*20)
    else:
        lis[lista[i][1]] += 1
print(count, time)
