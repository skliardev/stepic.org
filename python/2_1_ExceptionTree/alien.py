import re

def isParent(child, parent):
    return child == parent or any(map(lambda x: isParent(x, parent), dic[child]))

dic = {item[0] : item[1:] for item in [re.split("\W+", input()) for _ in range(int(input()))]}
exc_l = [i for i in (input() for _ in range(int(input())))]

for i in range(len(exc_l)):
    if any(map(lambda x: isParent(exc_l[i], x), exc_l[:i])): print (exc_l[i])
