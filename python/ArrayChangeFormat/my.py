a = []
# Заполним массив a
while True:
    s = input().split()
    if s[0] == 'end':
        break
    a.append(s)

# Запоминаем размеры массива SI x SJ
SI = len(a)
SJ = len(a[0])

# Преобразуем str -> int
for i in range(SI):
    for j in range(SJ):
        a[i][j] = int(a[i][j])

# Создаем новый массив SI x SJ
b = [[0 for j in range(SJ)] for i in range(SI)]

# Заполняем его в формуле из задания
for i in range(SI):
    for j in range(SJ):
        if (j == SJ - 1) and (i == SI - 1):
            b[i][j] = (a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][0])
        elif j == SJ - 1:
            b[i][j] = (a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0])
        elif i == SI - 1:
            b[i][j] = (a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j + 1])
        else:
            b[i][j] = (a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1])

# Выводим массив
for i in range(SI):
    for j in range(SJ):
        print(b[i][j], end=' ')
    print()


