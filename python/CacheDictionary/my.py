arr = input().lower().split()
d = {}

for i in arr:
    d[i] = d.get(i, 0) + 1

for i in d:
    print(i, d[i])