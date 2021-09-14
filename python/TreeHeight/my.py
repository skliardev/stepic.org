input('Enter data plz:\n')  # just skip
tree = [int(i) for i in input().split()]
cache = {}
cache_used = 0
height = 0

for vertex in range(len(tree)):
    stack = [vertex]  # push element
    # print('\nVertex:', vertex)
    for element in stack:
        next = tree[element]
        if next == -1:  # found root
            height = max(height, len(stack))
            # cache[vertex] = len(stack) old version
            for index in stack:
                # print('element stack:', index, 'size element:', height - stack.index(index))
                cache[index] = len(stack) - stack.index(index)
            break
        elif cache.get(next, -1) > 0:  # вершина найдена в кеше
            cache_used += 1
            length = len(stack) + cache[next]  # длинна до вершины дерева с учетом кеша
            height = max(height, length)       # выбираем самую глубокую вершину
            for index in stack:
                # print('element stack:', index, 'size element:', length - stack.index(index))
                cache[index] = length - stack.index(index)
            break
        else:
            stack.append(next)

print('\nThis statistic:')
print('cache:', cache)
print('cache used:', cache_used)
print('height:', height)
