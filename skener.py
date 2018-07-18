def scale(m,xf,yf):
    t= []
    for r in m:
        tr= ""
        for rc in r:
            for _ in range(yf):
                tr+=rc
        for _ in range(xf):
            t.append(tr)
    return t

r,c,zr,zc= map(int,input().split())
l = [input()for i in range(r)]
ls= scale(l,zr,zc)
print(*ls,sep="\n",end="\n")
