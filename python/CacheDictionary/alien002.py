s = input().lower().split()
for i in set(s):
    print(i, s.count(i))
