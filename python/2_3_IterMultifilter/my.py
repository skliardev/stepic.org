class multifilter:
    def judge_half(pos, neg):
        return True if pos >= neg else False

    def judge_any(pos, neg):
        return True if pos > 0 else False

    def judge_all(pos, neg):
        return True if neg == 0 else False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.jadge = judge

    def __iter__(self):
        arr = []
        for el in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(el):
                    pos += 1
                else:
                    neg += 1
            
            if self.jadge(pos, neg):
                arr.append(el)
        return iter(arr)