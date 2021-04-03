n = int(input())
suma= 0
fore = 0
if (n%2 == 0):
    i=0
    while i < n:
        temp=int(input())
        if i== 0:
            fore = temp
        else:
            suma =abs(fore-temp)
            fore = suma
            # print(fore,temp,i)

        i+=1
    print(suma)
else:
    print("still running")
