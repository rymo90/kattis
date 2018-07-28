class ArrayQ:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop()


q = ArrayQ()
l = 1
while True:
    lis = []
    count = 0
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n):
            temp = input()
            if count == 0:
                lis.append(temp)
                count = 1
            else:
                q.enqueue(temp)
                count = 0
        print("SET", l)
        l += 1
        print("\n".join(lis))
        while q.isEmpty() == False:
            a = q.dequeue()
            print(a)
