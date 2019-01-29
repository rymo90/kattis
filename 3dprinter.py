lis= []
n = int(input())
for i in range(15):
  lis.append(2**i)
for j in range(len(lis)):
  if n <=lis[j]:
    print(j+1)
    break
