n = int(input())
value= list(map(int,input().split()))
value = sorted(value)
alice = 0
bob= 0
#
if n == 1:
    alice += value.pop()
else:
    for i in range(n):
        if i%2 == 0:
             alice += value.pop()
        else:
            bob += value.pop()

print(alice,bob)
