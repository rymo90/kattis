jon = input()
doc= input()
count_a = 0
for i in range(len(doc)):
    if doc[i]== "a":
        count_a +=1
if doc[0] == "h":
    print("go")
else:
    if count_a > len(jon[:-1]):
        print("no")
    else:
        print("go")
