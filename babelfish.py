import sys
lines = sys.stdin.readlines()
dic= {}
count = True
for i in range(len(lines)):
    x= lines[i].replace("\n","")
    if count:
        if  x.strip():
            temp = x.split()
            dic[temp[1]] = temp[0]
        else:
            count = False
    else:
        try:
            print(dic[x])
        except Exception as e:
            print("eh")
