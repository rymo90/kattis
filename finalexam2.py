n = int(input())

i = 0
tmp= ""
counter =0 
while i < n:

    svr= input()
    if i == 0:
        tmp = svr
        i+=1
    else:
        if svr == tmp:
            counter += 1
        tmp = svr
        i+=1

print(counter)
