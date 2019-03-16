n = int(input())
lis= []
for _ in range(n):
    k = input().split()
    lis.append(k)
result= 0
for i in range(len(lis)-1):
    fst = lis[i]
    sec= lis[i+1]
    eq1= (float(fst[1])+float(sec[1]))/2
    eq2= int(sec[0])-int(fst[0])
    result += eq1*eq2
print(result*0.001)
