k = int(input())
fst= input()
sec= input()
gem= 0
for i in range(len(fst)):
    if fst[i] == sec[i]:
        gem +=1

a = abs(gem - k)

print(len(fst)-a)
