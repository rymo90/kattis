n = int(input())
for i in range(n):
    x = input()
    if "=" in x:
        print("skipped")
    else:
        for j in range(len(x)):
            if x[j] == "+":
                a = int(x[0:j])
                b = int(x[j + 1:])
                print(a + b)
