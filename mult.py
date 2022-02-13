n  = int(input())
lis = []
for i in range(n):
    tmp  = int(input())
    lis.append(tmp)

counter = 0
temp =0
while len(lis) > 0:
    if counter == 0:
        temp = lis.pop(0)
        counter +=1
    else:
        num = lis.pop(0)
        if num%temp == 0:
            print(num)
            counter = 0
            
