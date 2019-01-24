from collections import defaultdict
dic = defaultdict(int)
svar = []
a = input().split(" ")
num = int(a[-1])
a = "".join(a[:-1])
b= input()
found= True
if len(a) >=2:
    for i in range(len(a)-1):
        print(a)
        if a[i].isupper():
            temp= 0
            if a[i+1].isdigit():
                s= i
                while len(a[s:]) !=1 and a[s+1].isdigit():
                    temp+= int(a[s+1])
                    s+=1
            else:
                temp = 1
            if a[i] in dic:
                dic[a[i]]+= temp*num
            else:
                dic[a[i]] = temp*num

else:
    dic[a[0]] = num
print(dic)
if len(b) >= 2:
    for j in range(len(b)-1):
        if b[j].isupper():
            if b[j] in dic:
                continue;
                svar.append(2)
            else:
                print("not found")
                found= False
                break

#
else:
    if b in dic:
        svar.append(dic[b[0]]//1)
    else:
        found= False


if found:
    print((svar))
else:
    print(0)
