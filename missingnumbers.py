x = int(input())
prev =0
lis= []
for i in range(x):
    n = int(input())
    if prev+1 !=  n:
        k = prev+1
        while k != n:
            lis.append(k)
            k+= 1
        prev = k

    else:
        prev = n

if len(lis) == 0:
    print("good job")
else:
    for _ in lis:
        print(_)
