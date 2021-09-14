graph = {}
verificateEx = []

for child, *parents in [input().replace(':', '').split() for _ in range(int(input()))]:
    graph[child] = set(parents)
    graph[child].discard(child)     # исключаем самонаследование (не обязательно)

for exception in [input() for _ in range(int(input()))]:
    if verificateEx.count(exception):   # убираем дубликаты если текущее
        continue                        # то смысла в таком же нет, оно не будет обрабатываться

    curTreeEx = [exception]  # получаем текущего исключения-ребенка

    for select in curTreeEx:
        if verificateEx.count(select):  # если в списке родитель существует
            print(exception)            # то нет смысла в проверяемом исключении
            break
        else:                           # если нет то добавляем родителей в проверку
            curTreeEx += graph[select]
    verificateEx.append(exception)
