input()  # just skip
tree = [int(i) for i in input().split()]
cache = {}
height = 0  # максимальная грубина

for vertex in range(len(tree)):
    stack = [vertex]  # создаем стек вершин для поиска вершины дерева
    length = 0
    for element in stack:
        next = tree[element]
        if next == -1:  # найден корень
            length = len(stack)
        elif cache.get(next, -1) > 0:  # вершина найдена в кеше
            length = len(stack) + cache[next]  # длинна до вершины дерева с учетом кеша
        else:
            stack.append(next)
            continue
        height = max(height, length)  # выбираем самую глубокую вершину
        if len(stack) > 1:
            for index in stack:
                cache[index] = length - stack.index(index)
        break

print(height)
