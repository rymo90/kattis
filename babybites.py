x = int(input())
date= input().split()
for i in range(x):
    if date[i] == "mumble":
        date[i]= str(i+1)
result= True
for i in range(len(date)):
    if str(i+1) != date[i]:
        result= False
if result:
    print("makes sense")
else:
    print("something is fishy")
