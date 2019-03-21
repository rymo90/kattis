s = input().split(" ")
count= 0
word = 0
for i in range(len(s)):
    word +=1
    if "ae" in s[i]:
        count +=1
if (count*100/word) >=40:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
