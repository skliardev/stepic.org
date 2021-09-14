s = input().lower().split()
for k, v in {key: s.count(key) for key in s}.items():
    print("{} {}".format(k,v))