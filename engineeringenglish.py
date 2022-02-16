import sys
dict  = {}
svar = []
smobok = []
for line in sys.stdin:
    lista = line.split()
    for _ in range(len(lista)):
         check = lista[_].lower()
         if check not in smobok:
             smobok.append(check)
             svar.append(lista[_])
         else:
            svar.append(".")

print(*svar)
