n = int(input())
for i in range(n):
    b, p = [j for j in input().split()]
    bpm = 60 * float(b) / float(p)
    minBpm = bpm - (60 / float(p))
    maxBpm = bpm + (60 / float(p))
    print(minBpm, bpm, maxBpm)