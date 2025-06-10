class army: 
def func1(self):
print("the value of given term will 1st")
class nsg(army): 
def func2(self):
print("the value of given term will 2nd")
class para(nsg): 
def func3(self): 
print("the value of given term will 3rd")
object=para()
obj=input("enter the value of para")
print(obj)
object.func3()
