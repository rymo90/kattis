col,row,n= map(int,input().split())
lis= [[0]*row for i in range(col)]
space= row*col
col-=1
row-=1
count = 0
indx= []
for _ in range(n):
    c,r = map(int,input().split())
    c-=1
    r-=1
    tmp= str(c)+str(r)
    if tmp in indx:
        continue
    else:
        indx.append(str(c)+","+str(r))
        lis[c][r]=1
        space-=1
fst= len(indx)
sec= 0
while len(indx)!= 0 :
    num= indx.pop(0)
    num = num.split(",")
    fst-=1
    i,j = int(num[0]),int(num[1])
    lis[i][j]=2
    if j >0 :
        if lis[i][j-1]==0 :
            lis[i][j-1]=1
            space-=1
            sec +=1
            indx.append(str(i)+","+str(j-1))

    if j < row :
        if lis[i][j+1]==0:
            lis[i][j+1]= 1
            space-=1
            sec +=1
            indx.append(str(i)+","+str(j+1))
            


    if i >0 :
        if lis[i-1][j]==0:
            lis[i-1][j]=1
            space-=1
            sec +=1
            indx.append(str(i-1)+","+str(j))


    if i < col :
        if lis[i+1][j]==0:
            lis[i+1][j]= 1
            space-=1
            sec +=1
            indx.append(str(i+1)+","+str(j))
    if fst ==0:
        count +=1
        fst= sec
        sec= 0

print(count)
