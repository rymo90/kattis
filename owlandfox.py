n = int(input())
result = ""
for _ in range(n):
    s = list(input())
    if len(s) == 1:
        s[0] = str(int(s[0]) - 1)
        result = s
    else:
        if s[-1] == "0":
            for i in range(len(s) - 1, -1, -1):
                if s[i] != "0":
                    s[i] = str(int(s[i]) - 1)
                    result = s
                    break
        else:
            s[-1] = str(int(s[-1]) - 1)
            result = s
    if all(x == result[0] for x in result):
        if result[0] == "0":
            print(0)
        else:
            print("".join(result))
    else:
        print("".join(result))
