n = int(input())
namespace = {
    "global": {"parent": None, "let": []}
}
result = []

for index in range(n):
    INST, KEY, VALUE = input().split()
    if INST == 'create':
        if KEY in namespace:
            print("Namespace already exists")
        else:
            namespace[KEY] = {"parent": VALUE, "let": []}
    elif INST == 'add':
        if KEY not in namespace:
            print("Namespace does not exist")
        else:
            namespace[KEY]["let"].append(VALUE)
    else:
        TKEY = KEY
        while True:
            if TKEY is None:
                result.append(None)
                break
            elif VALUE in namespace[TKEY]["let"]:
                result.append(TKEY)
                break
            else:
                TKEY = namespace[TKEY]["parent"]

[print(line, namespace[line]) for line in namespace]
[print(name) for name in result]