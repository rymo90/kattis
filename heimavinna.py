txt = input()
svd = []
koma = -1
for i in range(len(txt)):
    if txt[i]== ";":
        tmp= ""
        if koma == -1:
            koma = 0
            while koma < i :
                tmp += txt[koma]
                koma+=1
            koma = i+1
        else:
            while koma < i:
                tmp += txt[koma]
                koma +=1
            koma = i+1

        svd.append(tmp)

if koma == -1:
    svd.append(txt)
else:
    svd.append(txt[koma:])
counter = 0
for j in range(len(svd)):
    num = 0;
    try:
        num = svd[j].index("-")
    except ValueError:
        counter += 1
    else:
        ll = svd[j]
        counter += abs(int(ll[0:num]) - int(ll[num+1:]))+1
print(counter)
