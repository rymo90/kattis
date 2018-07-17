s= int(input())
i = 3
print(s,end="")
print(":")
while i <= s:
    secRow= i//2
    fstRow = i -secRow
    if s%i==0 or s%i == fstRow :
        print(fstRow,end=",")
        print(secRow)
    i+=1
