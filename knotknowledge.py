n = input()
x= input().split()
y = input().split()

for i in range(len(x)):
    if x[i] not in  y:
        print(int(x[i]))
