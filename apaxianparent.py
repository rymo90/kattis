x = input().split()
vowel = "aiou"
svar = ""
lst= x[0][-1]
lst2=x[0][-2:]
if lst2 == "ex":
    svar = x[0]+x[1]
else:
    if lst == "e":
        svar = x[0]+"x"+x[1]
    elif lst in vowel:
        svar = x[0][0:-1]+"ex"+x[1]
    else:
        svar = x[0]+"ex"+x[1]    
print(svar)
