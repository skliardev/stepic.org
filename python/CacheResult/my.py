# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
def f(x):
    return x*x


n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x not in d:
        d[x] = f(x)
    print(d[x])