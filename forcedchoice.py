n,secret,steps = map(int,input().split())
cards = []
for i in range(n):
    cards.append(i+1)
for j in range(steps):
    predict = list(map(int,input().split()))
    choice = predict[1:]
    m = predict[0]
    if secret not in choice:
        for _ in range(m):
            cards.remove(choice[_])
        print("REMOVE")
    else:
        cards = choice
        choice= []
        print("KEEP")
