def jemnaUdda(lista):
    dict = {"uj": "u","uu": "j","jj":"j","ju":"u" }
    svar= ""
    tmporar = ""

    for j in range(len(lista)):
        if j == 0:
            tmporar =lista[j]
        else:
            svar = dict[tmporar+lista[j]]
            tmporar = svar

    return tmporar
n = int(input())
di2 = {"u":"j","j":"u"}
lista = []
for i in range(n):
    if (i+1)%2 == 0:
        lista.append("j")
    else:
        lista.append("u")
lastpeace = ""
if n%2 == 0:
    lastpeace = di2["j"]
else:
    lastpeace = di2["u"]

listvo  = lista[1:]
listvo.append(lastpeace)
sv1 = jemnaUdda(lista)
sv2 = jemnaUdda(listvo)
if sv1 != sv2:
    print("Either")
else:
    if sv1== "u":
        print("Odd")
    else:
        print("Even")
