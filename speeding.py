n = int(input())
newtime,newdistance = 0,0

time = []
distance = []
svar = 0
for i in range(n):
    dist=list(map(int,input().split()))
    time.append(dist[0])
    distance.append(dist[1])


svar = []
while n  > 0:
    x0= distance.pop(0)
    t0= time.pop(0)
    for i in range(len(distance)):
        velocity = 0
        x1= distance[i]
        t1= time[i]
        velocity = (x1-x0)//(t1-t0)
        svar.append(velocity)
    n-=1
print(max(svar))
