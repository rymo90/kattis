prices = [0 ,*map(int, input().split())]
trucks = [tuple(map(int, input().split())) for _ in range(3)]
start = [t[0] for t in trucks]
end = [t[1] for t in trucks]
current_trucks= 0
price= 0
for i in range(min(start), max(end)+1):
    current_trucks += start.count(i)
    current_trucks -= end.count(i)
    price+= prices[current_trucks]* current_trucks

print(price)
