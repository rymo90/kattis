t  = int(input())
run = True
while t > 0  :
    s = input().split()
    sv=0
    before= 1
    for i in s:
        if i == "0":
            break
        else:
            sample= int(i)
            if sample <= before*2:
                before= sample
            else:
                sv+= abs(sample-before*2)
                before= abs(sample-before+before)
    print(sv)
    t-=1
