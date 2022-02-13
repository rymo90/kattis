l = input()
n = int(input())
for _ in range(n):
    s = input()
    tmp = 0
    if l[0] in s:
        for i in range(len(s)):
            if s[i] not in l:
                break
            else:
                tmp += 1
    if tmp == len(s) and tmp >= 4:
        print(s)
