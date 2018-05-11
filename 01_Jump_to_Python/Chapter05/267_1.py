class Calculator:
    def __init__(self, num):
        self.num = num

    def sum(self):
        result = 0
        for i in self.num:
            result += i
        return result

    def avg(self):
        result = 0
        for i in self.num:
            result += i
        return result / len(self.num)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())