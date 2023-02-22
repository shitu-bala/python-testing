class imp :
     num=70
     res = 0
     def __init__(self):
         print("inside constructor")
     def getdata(self):
         print("this is my first project ")
     def add(self,a,b):
         self.res =a+b
         return self.res
     def div(self,a):
         result= self.res/a
         return result

obj= imp()
obj.getdata()
res2 = obj.add(22,78)
print(obj.num)
print(obj.res)
print(res2)
print(obj.div(10))