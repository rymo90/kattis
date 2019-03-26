import sys
for line in sys.stdin:
    data= line.rstrip().split()
    fore = "".join(data[-2:-1]).split(":")
    efter = "".join(data[-1:]).split(":")
    data = data[:-2]
    foreHour = int(fore[0])*60
    foreMin = int(fore[1])
    efterHour = int(efter[0])*60
    efterMin = int(efter[1])
    hour = round((efterHour-foreHour)/60)
    minute = (efterMin-foreMin)
    if foreHour <= efterHour:
        if foreMin <= efterMin:
            print(*data,hour,"hours",minute,"minutes")
        else:
            print(*data,hour-1,"hours",minute+60,"minutes")
    else:
        if foreMin <= efterMin:
            print(*data,hour+24,"hours",minute,"minutes")
        else:
            print(*data,hour+23,"hours",minute+60,"minutes")
