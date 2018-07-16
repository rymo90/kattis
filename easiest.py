last = False
while not last:
    n= input()
    if n == "0":
        last = True
    else:
        sm= 0
        for i in n:
            sm+= int(i)
        stop= False
        p = 11
        while not stop:
            cnt= 0
            sum = str(p * int(n))
            for j in sum:
                cnt += int(j)
            if cnt == sm:
                print(p)
                stop= True
            else:
                p+= 1
