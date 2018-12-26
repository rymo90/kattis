n = int(input())
dic= []
for _ in range(n):
    employ= input().split()
    if employ[0] =="entry":
        if (employ[1] in dic):
            print(employ[1], "entered (ANOMALY)")
        else:
            dic.append(employ[1])
            print(employ[1], "entered")
    else:
        if employ[1] in dic:
            print(employ[1],"exited")
            dic.remove(employ[1])
        else:
            print(employ[1],"exited (ANOMALY)")
