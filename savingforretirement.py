B,Br,Bs,A,As = map(int,input().split())
svBob= abs(Br-B)*Bs
while svBob >=0:
    A+=1
    svBob -= As
print(A)
