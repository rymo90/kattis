s = list(map(int,input().split()))
while s != sorted(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            s[i], s[i+1] = s[i+1] ,s[i]
            print(*s)
