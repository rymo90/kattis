A = 0
B = 0
str= input()
for i in range(len(str)-1):
    if str[i]== "A":
        A += int(str[i+1])
    if str[i]== "B" :
        B += int(str[i+1])
if A > B:
    print("A")
else:
    print("B")
