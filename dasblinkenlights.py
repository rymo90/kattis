p,q,s = map(int,input().split())
l1 = [0]*s
l2 = [0]*s
jm= p
jm2 = q
svar=""
for i in range(s):
    if i+1 == p:
        l1[i] = 1
        p += jm
    if i+1 == q:
        l2[i] = 1
        q += jm2
for j in range(s):
    if l1[j] == 1 and l2[j]== 1:
        svar = "yes"
        break

if svar=="":
    print("no")
else:
    print("yes")    
