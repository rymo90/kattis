p,t= map(int,input().split())
count= 0
result = 0
for _ in range(p):
  for _ in range(t):
    s= input()
    found = True
    for i in range(len(s)):
      if s[i].isupper():
        if i == 0:
          continue
        else:
          found = False
    if found:
      count += 1
  if count == t:
    result += 1
  count = 0  
print(result)        
