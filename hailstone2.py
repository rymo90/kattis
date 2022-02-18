n  = int(input())
start = True
count = 0
while start:
    if n == 1:
        start = False
    else:
        if n%2 ==0 :
            n = n/2
        else:
            n = (3*n)+1
    count += 1
print(count)
