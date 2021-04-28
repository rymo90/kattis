a,b,c,d= map(int, input().split())
ac = a-c
bd = b-d

if ac >= 2 and bd >= 2 :
    print(1)
else:
    print(0)
