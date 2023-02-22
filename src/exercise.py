class employee:


    def __init__(self , name, last,  pay):
        self.firstname = name
        self.lastname = last
        self.pay = pay
        self.email = name +" ."+ last +"@gmail.com"
    def empdetail(self):
         return "{} {} {} {} ".format(self.firstname , self.lastname,self.pay,self.email)
   # def __str__(self):
        #return "{} {} with pay of ${}".format(self.firstname, self.lastname, self.pay)

e1 = employee ("arun", "verma", 5000)
print(e1.empdetail())
print(e1.__dict__)
print(e1)







