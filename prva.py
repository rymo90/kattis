
r, c = [int(i) for i in input().split()]
lis = []
allword = []
result = []
for _ in range(r):
    word = input()
    allword.append(word)
    lis.append(word)
for row in zip(*lis):
    test = "".join(row)
    allword.append(test)

for i in range(len(allword)):
    test = allword[i]

    if "#" in test:
        a = test.split("#")
        for j in range(len(a)):

            if len(a[j]) >= 2:

                result.append(a[j])

    else:
        result.append(test)
result = sorted(result)
print(result[0])
