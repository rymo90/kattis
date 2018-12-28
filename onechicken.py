n,m=map(int, input().split())
tst= abs(n-m)
if n <m:
    if tst > 1:
        print("Dr. Chaz will have "+str(tst)+" pieces of chicken left over!")
    else:
        print("Dr. Chaz will have "+str(tst)+" piece of chicken left over!")
else:
    if tst >1:
        print("Dr. Chaz needs "+str(tst)+" more pieces of chicken!")
    else:
        print("Dr. Chaz needs "+str(tst)+" more piece of chicken!")    
