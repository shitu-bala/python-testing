class Room1:

    def __init__(self, a, b):
        self.length = a
        self.width = b

    def area(self):
        return self.length * self.width


class Room2:
    def __init__(self,c,d):
        self.length = c
        self.width = d

    def area2(self):
        return self.length + self.width



E1 = Room1(5, 6)
E2 = Room2(20,40)
print(E1.area())
print(E2.area2())
