dic = {"a":2,"b":22,"c":222,"d":3,"e":33,"f":333,"g":4,"h":44,"i":444,"j":5,"k":55,"l":555,"m":6,"n":66,"o":666,"p":7,"q":77,"r":777,"s":7777,"t":8,"u":88,"v":888,"w":9,"x":99,"y":999,"z":9999, " ":0}
n  = int(input())

for _ in range(n):
  word= input()
  result = []
  if len(word) > 1:
    for i in range(len(word)-1):
      fst,sec= str(dic[word[i]]),str(dic[word[i+1]])
      if fst[0] == sec[0]:
        result .append(fst)
        result .append(" ")
      else:
        result.append(fst)

    if result[-1] != sec:
      result.append(sec)
  else:
    result.append(str(dic[word]))
   
  print("Case #"+ str(_+1)+":"+ " "+ "".join(result))      
