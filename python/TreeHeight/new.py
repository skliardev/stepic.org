input('Enter data plz:\n')
# input()  # just skip
tree = [int(i) for i in input().split()]
cache = {}
cache_used = 0  # сколько раз использовался кеш
cache_wr = 0  # сколько раз записывался кеш
jumping = 0  # сколько элементов перебрали
height = 0  # максимальная грубина

for vertex in range(len(tree)):
    stack = [vertex]  # создаем стек вершин для поиска вершины дерева
    length = 0
    for element in stack:
        next = tree[element]
        if next == -1:  # найден корень
            length = len(stack)
        elif cache.get(next, -1) > 0:  # вершина найдена в кеше
            cache_used += 1
            length = len(stack) + cache[next]  # длинна до вершины дерева с учетом кеша
        else:
            jumping += 1
            stack.append(next)
            continue
        height = max(height, length)  # выбираем самую глубокую вершину
        if len(stack) > 1:
            for index in stack:
                cache_wr += 1
                cache[index] = length - stack.index(index)
        break

print('\nThis statistic:')
print('cache:', cache)
print('cache used:', cache_used)
print('cache writing:', cache_wr)
print('Vertex jumping:', jumping)
print('Total use:', cache_wr + jumping)
print('height:', height)
