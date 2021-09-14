input()  # just skip
tree = [int(i) for i in input().split()]
height = 0  # максимальная грубина

for vertex in range(len(tree)):
    stack = [vertex]  # создаем стек вершин для поиска вершины дерева
    for element in stack:
        if tree[element] == -1:  # найден корень
            height = max(height, len(stack))
            break
        else:
            stack.append(tree[element])

print(height)
