k,r = tuple(map(int,input().split()))
parts= set()
for i in range(r):
  parts.add(input())
  if len(parts) == k:
    print(i+1)
    break
else:
  print("paradox avoided")    
