class MoneyBox:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return True if (self.count + v) <= self.capacity else False

    def add(self, v):
        self.count += v if MoneyBox.can_add(self, v) else 0


a = MoneyBox(5)
a.add(4)
print(a.count)
print(a.capacity)
print(a.can_add(1))
a.add(2)
print(a.count)
print(a.can_add(1))
