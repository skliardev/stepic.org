with open(input('Введите имя файла:')) as inf, open('out.txt', 'w') as ouf:
    stack = []
    for line in inf:
        stack.append(line)
    while len(stack):
        ouf.write(stack.pop())
    ouf.flush()
