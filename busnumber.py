n = int(input())
lis= list(map(int, input().split()))
lis.append(10000)
lis = sorted(lis)
result= []
count= 0 

for i in range(len(lis)-1):
  if abs(lis[i]-lis[i+1])==1:
    count+=1
  else:
    if count ==1:
      result.append(lis[i-1])
      result.append(lis[i])
    elif count > 1:
      result.append('{}-{}'.format(lis[i-count],lis[i]))
    else:
      result.append(lis[i])  
    count= 0
print(*result)


