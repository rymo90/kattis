n,h,v= input().split()
n = int(n)
h = int(h)
v = int(v)
if h == 0:
    h = 1
if v == 0:
    v = 1    
c1 = v*h*4
c2 = (n-h)* v * 4
c3 = (n-v)*h * 4
c4 = (n-v)*(n-h)*4
lista = [c1,c2,c3,c4]
print(max(lista))
