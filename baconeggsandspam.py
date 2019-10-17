
start = True
while start:
    dict = {}
    lis = []
    x= int(input())
    if x == 0:
        start = False
    else:
        for _ in range(x):
            k = input().split(" ")
            dict[k[0]] = k[1:]
            for _ in k[1:]:
                if _ in lis:
                    continue
                else:
                    lis.append(_)
        lis = sorted(lis)

        for j in range(len(lis)):
            lis2 = []
            for key in dict:
                if lis[j] in dict[key]:
                    lis2.append(key)
            lis2 = sorted(lis2)        
            print(lis[j], *lis2)

        print("")
