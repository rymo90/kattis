n = int(input())
for _ in range(n):
    data = input().split()
    name= data[0]
    temp= data[1]
    postSecondStudieYear = temp[0:4]
    temp2= data[2]
    bithYear= temp2[0:4]
    course= data[3]

    if int(postSecondStudieYear) >= 2010 or int(bithYear) >= 1991:
        print(name+" "+"eligible")
    else:
        if int(course) > 40:
            print(name+" "+"ineligible")
        else:
            print(name+" "+"coach petitions")
            
