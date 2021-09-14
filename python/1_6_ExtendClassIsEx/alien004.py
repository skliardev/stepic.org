n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def dfs(v, used):
    used.add(v)
    for i in parents[v]:
        if i not in used:
            dfs(i, used)

q = int(input())
for _ in range(q):
    a, b = input().split()
    used = set()
    dfs(b, used)
    print("Yes" if a in used else "No")