n = int(input())
counter = 7
for _ in range(n):
    a =  input()
    if a == "Skru op!" :
        if  counter <=9 :
            counter += 1
    else:
        if counter >=1:
            counter -= 1
print(counter)
