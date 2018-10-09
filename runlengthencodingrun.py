
x = input()
fst = x[0]
msg = x[2:]
result=""
dic = {}
lis = []
count= 1
if fst == "D":
    for i in range(len(msg)):
        if msg[i].isdigit():
            result += msg[i-1] *int(msg[i])

else:
    msg= msg+"**"
    for j in range(1, len(msg)):
        if msg[j] == msg[j-1]:
            count += 1
        else:
            result += msg[j-1]+str(count)
            count = 1
print(result)
