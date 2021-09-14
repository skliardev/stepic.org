class treedist(dict):
    def addClass(self, klass, children):
        self[klass] = set(children)
        self[klass].discard(klass)

    def isChild(self, klass, child):
        if child not in self:
            return False
        lst = list()
        lst.append(child)
        for sel in lst:
            # print('Find:', klass, '(', child, ')')
            # print('Select:', sel)
            # print('List:', lst, '\n')
            if klass in self[sel] or klass == child:
                return True
            else:
                lst += self[sel].difference(set(lst))
        return False


dl = treedist()

for klass, *args in [input().replace(':', '').split() for _ in range(int(input()))]:
    dl.addClass(klass, args)

for klass, base in [input().split() for _ in range(int(input()))]:
    if dl.isChild(klass, base):
        print('Yes')
    else:
        print('No')
