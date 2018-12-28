a,b,c= map(int,input().split())
left= abs(a-b)
right = abs(b-c)
count = 0
if right >= left:
    while b+ 1< c:
        count +=1
        b+=1
    print(count)
else:
    while a+1 < b:
        count +=1
        a+=1
    print(count)
