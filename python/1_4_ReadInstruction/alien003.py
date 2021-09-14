def create(namespace, parent):
    namespaces.update({namespace: [parent]})


def add(namespace, var):
    namespaces[namespace] += [var]


def get(namespace, var):
    while not namespace is None and var not in namespaces[namespace]:
        namespace = namespaces[namespace][0]
    print(namespace)


namespaces = {'global': [None]}
commands = {'create': create, 'add': add, 'get': get}
n = int(input())
for _ in range(n):
    enter = input().split()
    commands[enter[0]](enter[1], enter[2])