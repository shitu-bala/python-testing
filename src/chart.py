from arjun import employee


class Chart(employee):
    num2 = 200
    def __init__(self):

      employee.__init__(self,5,9)

    def completedata(self):
        return self.num2 + self.num + self.addition()


e3 = Chart()
print(e3.completedata())

