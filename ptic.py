#zip and dictinary was used in this exercise!

s = int(input())
n = input()
namn = {
    "Adrian": "ABC",
    "Bruno": "BABC",
    "Goran": "CCAABB",
}
points = {}

for lad in namn:
    lad_pts = 0
    for ans, guess in zip(n, namn[lad] * s):
        if ans == guess:
            lad_pts += 1
    points[lad] = lad_pts
best = max(points.values())
print(best)
for lad in sorted(points):
    if points[lad] == best:
        print(lad)