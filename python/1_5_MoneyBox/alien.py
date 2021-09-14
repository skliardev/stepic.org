class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity >= v

    def add(self, v):
        self.capacity -= v
