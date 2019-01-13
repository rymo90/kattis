n= int(input())
for _ in range(n):
  ck= 1
  x= list(map(int,input()))[::-1]
  for i in range(len(x)):
    if i == ck:
      num= x[i]*2
        
      if num > 9:
        while num > 9:
          res= 0
          for k in list(map(int,str(num))):
              res+= int(k)
          num = res
        x[i]= num      
      
      x[i]= num
      ck+=2 
  if sum(x)%10==0:
    print("PASS")
  else:
    print("FAIL")                         

        
