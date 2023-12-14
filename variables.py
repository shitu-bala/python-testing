class Emp:
    def __init__(self,eid,Ename,salary):
        self.eid= eid
        self.Ename=Ename
        self.salary=salary
    def display(self):
        print(self.eid,self.Ename,self.salary)
E1= Emp(101,"Ayaan",25000)
E2= Emp(102,"Arjun",30000)
E1.display()
E2.display()



