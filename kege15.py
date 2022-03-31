class HolidayEve:
    def __init__(self, n):
        self.n = n[:]
        self.c = 0

    def add_mood(self, other):
        self.n.append(other)
        return 'Mood added'

    def show_long(self):
        count = 0
        for i in range(self.n):
            count += len(self.n[i])
        self.c = count // len(self.n)
        v = []
        for elem in self.n:
            if len(elem) > self.c:
                v.append(elem)
        return sorted(v)

    def show_short(self):
        count = 0
        for i in range(self.n):
            count += len(self.n[i])
        self.c = count // len(self.n)
        v = []
        for elem in self.n:
            if len(elem) <= self.c:
                v.append(elem)
        return sorted(v).reverse()

