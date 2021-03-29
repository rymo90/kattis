txt = input()
num = len(txt)//3
tst1 = ""
tst2= ""
tst3= ""
for i in range(len(txt)):
    if i < num:
        tst1 += txt[i]
    elif i == num or i < (num+num):
        tst2 += txt[i]
    else:
        tst3 += txt[i]


if tst1 == tst2:
    print(tst1)
elif tst1 == tst3:
    print(tst1)
else:
    print(tst2)
