start = True
result = []
while start:
    list1= []
    list2 = []
    temp = []
    dic = {}
    x = int(input())
    if x== 0:
        break

    else:

        for i in range(x*2):
            n = int(input())
            if i > x-1:
                list2.append(n)
            else:
                temp.append(n)
                list1.append(n)
        list1= sorted(list1)
        list2= sorted(list2)
        for j in range(len(list1)):
            dic[list1[j]] =list2[j]

    for k in temp:
        result.append(dic[k])
    result.append("")
for res in result[:-1]:
    print(res)
