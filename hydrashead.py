while True:
    s= raw_input()
    h= int(s[0]) 
    t = int(s[1])
    if h==0 and t== 0:
        break
    moves= 0
    if t == 0:
        moves = -1
    else:
        while True:
            head= h+t//2
            if(t%2 and head%2==0):
                moves+= t//2
                moves+= head//2
                break
            t+=1
            moves+=1
    print moves 
