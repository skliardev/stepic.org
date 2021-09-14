nam = {'global': {'par': None, 'vrs': set()}}

for x in [input().split() for cmd in range(int(input()))]:
    if x[0] == 'create':
        nam[x[1]] = {'par': x[2], 'vrs': set()}
    elif x[0] == 'add':
        nam[x[1]]['vrs'].add(x[2])
    elif x[0] == 'get':
        get = lambda n, v: v in nam[n]['vrs'] and n or n == 'global' and 'None' or get(nam[n]['par'], v)
        print(get(x[1], x[2]))