from group import hashlib
import math
import hashlib
class group:
     a="mahesh"
     b="sager"
     c="vikram"
     
     def __init__(self,x1,y1,z1):
         self.x1=x1
         self.y1=y1
         self.z1=z1
         
  # I will Crack cds AIR 1 with marks 300/300
  '''I have been shouting since 2023 I have to join many of the desire'''
  group=obj(a:"mahesh" ,b:"sager" ,c:"vikram")
  print(group)     
  
try:
      print("the value will be all a and b")
      
else:
    print("nothing will print")    
    
 except as value b:
     print("use values among b")
     
finally:      
    print("use other case") 
    
    def solve(s):
        s='''the valuevof given func and all given to sets'''
        print(solve.__doc__(s))
        print(f"the value of given {1} and {3}")
        
if a==b:
    break
    print("a is equal to b")
    
else if:
    break
    print("a is greater than b")
    
else:
    print("a is not equal to b")
    
print(a==x1)
print(a is y1)

  if a!=b["sager"]: print("a will\nnot work")
  else: print("a will works")
  
for c in c:
    print(c)
    
 else:
     print("other a and b")
     
 if __"name"__==__"main"__    
          print("use main method")
          
 else:
     print("use case others")
     
 print(str(a)+str(b))
            
  while(__"name"__==__"main"__):
      print("will be continue statement")
      
 str(a)=input("enter the value of str(a)")
 print(a)
    
          e=518
          p=1000
          print(e)
          
          def excuse(r):
          r=12.84
          print(r)
               
         print(p)
   
    dict={q:"salman khan",v:"akshay kumar",l:"vidut jamwal"}  
    print(dict)
     dict.pop(q)
     print(dict)
     del v[2]:
     print(v)
     
     def cube(j=5):
         
         lambda j:j*j*j
         print(lambda(j))
         
    class proccess:
        def __init__(self,reproduce,create):
            self.n1=n1
            self.n2=n2
            
     @staticmethod 
     def contain(w=52):
         return w
         
   if __init__="__main__": 
      print("enter the value of w")  
      
   else:
       print("other case")
    
 name="srushti" 
 print(name)
 print(name[0:3])
 print(name[-1:4])
 print(name.upper)
 print(name.lower)
 print(name.repalce)
 print(len(name[2:5]))  
                       
tuple=(53,73,73.81,100)
print(tuple)   
print(type(tuple))
print(len(tuple))
print(tuple[4:-1])
                    
  def factorial(s=7):
      return fact(7):

# program to illustrate public access modifier in a class


class Geek:

    # constructor
    def __init__(self, name, age):

        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):

        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("R2J", 20)

# finding all the fields and methods which are present inside obj
print("List of fields and methods inside obj:", dir(obj))

# accessing public data member
print("Name:", obj.geekName)

# calling public member function of the class
obj.displayAge()
  
# program to illustrate private access modifier in a class

class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):

        # accessing private data members
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    # public member function
    def accessPrivateFunction(self):

        self.__displayDetails()
obj = Geek("R2J", 1706256, "Information Technology")

print(dir(obj))
print("")
print(obj._Geek__name)
print(obj._Geek__roll)
print(obj._Geek__branch)
obj._Geek__displayDetails()

print("")
obj.accessPrivateFunction()                      
               
               # program to illustrate protected access modifier in a class

# super class
class Student:

    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):

        # accessing protected data members
        print("Roll:", self._roll)
        print("Branch:", self._branch)
