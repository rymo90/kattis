while True:
    numerator, denominator = map(int, input().split())
    if numerator == 0 and denominator == 0:
        break
    else:
        holenum= numerator//denominator
        reminder= numerator%denominator
        mixFraction= str(reminder) + " / " + str(denominator)
        print(holenum, mixFraction) 
