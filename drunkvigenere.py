import string
alphabet = string.ascii_uppercase
alphabet = list(alphabet)
msg = input()
key= input()
svar = ""
for i in range(len(msg)):
    a  = alphabet.index(msg[i])
    b  = alphabet.index(key[i])
    idx= 0
    if i%2== 0:
        idx = (a-b)%26
    else:
        idx= (a+b)%26
    svar += alphabet[idx]
print(svar)          
