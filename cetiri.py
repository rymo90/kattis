ls = sorted(list(map(int, input().split())))
a = abs(ls[0]-ls[1])
b= abs(ls[1]-ls[2])
if a == b:
    if ls[2] + a > 100:
        print(ls[0]-a)
    else:
        print(ls[2]+a)
else:

    if a < b:
        m= ls[1]
        r = ls[2]
        while m  < r:
            tst= abs(ls[1]-(m+1))

            if tst == a:
                print(m+1)
                break
            m+=1

    else:
        l = ls[0]
        m = ls[1]
        while l < m:
            tst = abs(ls[0]-(l+1))
            if tst == b:
                print(l+1)
                break
            l+=1
