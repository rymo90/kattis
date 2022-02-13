n = int(input())
i = 0
svar = 0
while i < n:
    a = input()
    a = a.lower()
    if "pink" in a or "rose" in a:
        svar += 1

    i += 1
if svar==0:
    print("I must watch Star Wars with my daughter")
else:
    print(svar)    
