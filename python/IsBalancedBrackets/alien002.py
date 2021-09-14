def check(st):
    pos = []
    pairs = {')': '(', '}': '{', ']': '['}
    for i, c in enumerate(st, 1):
        if c in pairs.values():
            pos.append(i)
        elif c in pairs and (not pos or st[pos.pop()-1] != pairs[c]):
            return i
    return pos.pop() if pos else "Success"


print (check(input()))