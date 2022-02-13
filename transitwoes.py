start,stop,n= map(int,input().split())
distance = list(map(int,input().split()))
rideTime = list(map(int,input().split()))
arriveTime = list(map(int,input().split()))
svar = ""
counter = 0
newtime =0
if start >= stop:
    svar= "no"
else:
    for i in range(n):
        counter += distance[i]
        if counter<= arriveTime[i]:
            counter +=  + abs(distance[i]-arriveTime[i])+ rideTime[i]
        else:
            newtime = arriveTime[i]
            while counter > newtime:
                newtime += newtime
            counter += abs(counter-newtime) + rideTime[i]
counter += distance[-1]
if counter > stop:
    print("no")
else:
    print("yes")    
