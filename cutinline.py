n = int(input())
lista = []
for _ in range(n):
    a = input()
    lista.append(a)
s = int(input())
for _ in range(s):
    mv = input().split()
    start = mv[0]
    if start == "cut":
        lista.insert(lista.index(mv[2]),mv[1])
    else:
        lista.remove(mv[1])
        
for k in lista:
    print(k)
