namespace = {
    "global": {"parent": None, "let": []}
}
result = []

for inst, key, value in [input().split() for _ in range(int(input()))]:
    if inst == 'create':
        if key not in namespace:
            namespace[key] = {"parent": value, "let": []}
    elif inst == 'add':
        if key in namespace:
            namespace[key]["let"].append(value)
    else:
        tmp = key
        while not tmp is None and value not in namespace[tmp]["let"]:
            tmp = namespace[tmp]["parent"]
        result.append(tmp)

[print(name) for name in result]