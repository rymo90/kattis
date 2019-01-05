import sys
lines = sys.stdin.readlines()
for i in range(len(lines)):
    x = lines[i].replace("\n","")
    temp = "".join(x)
    if "problem" in temp.lower():
        print("yes")
    else:
        print("no")
    
