from idlelib.pyshell import fix_x11_paste
from traceback import print_tb
import math
import hashlib
class  value:
    def __init__(self,freinds,relatives):
        self.freinds=freinds
        self.relatives=relatives

        def _repr_(self):
            return repr(__obj=str)

        if __name__=='__main__':
            str=0
            str="indian gorkha"
            str=len("__obj")
            print(str)
            print(str[2:-1])
            print(str(len("__obj")))
            print(str.uppercase(str))
            print(str.lowercase(str))
            print(str.istitle(str))
for str in range(5):
    if(str==5):
        break
    else:
        break

print("str will be")
print("str will not be")

def fact(t=85):
    return t*t

print(fact())
if fact()==85:  print("factorial will have")
else:print("fact will not have")

def solve(p=7856):
    '''the valueof given the term'''
try:
 print(solve().__doc__)

except:
 print(f"solve others __doc__")

finally:
     print("no other")
          # indian army can beat 1000 pepole at time without use gun
     a=765
     b=932
     print(int(a)+int(b))

print(a==b)
print(a is b)
print(a!=b)
a=input("enter the  value\n of a and b")
print(a)
print(b)
for a in a:
    print(a)

while(a==5):
    continue

else:
    print("use b method")

solve=lambda  p:p*p
print(solve)
for p in enumerate("7856"):
    print(p)

files={a:"mumbai",b:"hydrabad"}
print(files)
print(files.get)
#print(files.value())
print(files.keys)

class city:
 def __init__(self,m1,h1):
   self.m1=m1
   self.h1=h1

def show(self,mumbai,hydrabad):
         print("usde the  value of f{m1}  and {h1}")

         def my_alternativeconstructer():
             return obj

obj=city.my_alternative(show("m1","h1","hydrabad"))
print(obj)

def railway(station):
        match station:
           case "csmt":
             print("use A")

           case"pune jn":
            print("use B")

           case "dader central":
                print("use C")
        print("use A")
        print("use B")
        print("use C")

f=[64,82,194,945]
print(f[1:3])
print(len(f))
f.reverse()
f.append(56)
f.index(89)

tuple=(75,891,9665,84)
print(type,(tuple))
print(tuple[3:-2])
x=tuple.index(49)
q=tuple.count(1000)
print(q)
print(x)
g={75,84,832}
print(g)
print(type(g))
print(g.issuperset(g))
print(g.union())
print(g.intersection())

msg=input("enter the value of msg")

for msg in msg:
 raise stringerror
 print(msg)
 folders=math.listdir("data")
 print(folders)

 e=5734
 def use(i=75):
     print(i)

     print(e)
f=open("file.txt"'rw')
text=f.read()
print(text)

k=0
line=k.read
print(line.read(k))
files=z.readline(z)
print(files)
with open('file.txt','rw')  as f:
    print(type(f))
    s.seek(64)
    s.tell(81)

def  cube(te):
  te=[75,834,9342,9405]
  newl=list(map(cube,te))
  print(te)
  newl=list((cube(te)))
  print(newl)

  def  marks(max):
      def __init__(self):
          @decorater
      def  mfx():
          return mfx()

      class Geek:
          def __init__(self, age=0):
              self._age = age

          # getter method
          def get_age(self):
              return self._age

          # setter method
          def set_age(self, x):
              self._age = x

      raj = Geek()

      # setting the age using setter
      raj.set_age(21)

      # retrieving age using getter
      print(raj.get_age())

      print(raj._age)

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

      # derived class
      class Geek(Student):

          # constructor
          def __init__(self, name, roll, branch):
              Student.__init__(self, name, roll, branch)

          # public member function
          def displayDetails(self):
              # accessing protected data members of super class
              print("Name:", self._name)

              # accessing protected member functions of super class
              self._displayRollAndBranch()

      stu = Student("Alpha", 1234567, "Computer Science")
      print(dir(stu))

      # protected members and methods can be still accessed
      print(stu._name)
      stu._displayRollAndBranch()

      # Throws error
      # print(stu.name)
      # stu.displayRollAndBranch()

      # creating objects of the derived class
      obj = Geek("R2J", 1706256, "Information Technology")
      print("")
      print(dir(obj))

      # calling public member functions of the class
      obj.displayDetails()

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
              # accessing private member function
              self.__displayDetails()

      # creating object
      obj = Geek("R2J", 1706256, "Information Technology")

      print(dir(obj))
      print("")

      # Throws error
      # obj.__name
      # obj.__roll
      # obj.__branch
      # obj.__displayDetails()

      # To access private members of a class
      print(obj._Geek__name)
      print(obj._Geek__roll)
      print(obj._Geek__branch)
      obj._Geek__displayDetails()

      print("")

      # calling public member function of the class
      obj.accessPrivateFunction()

      class MyClass:
          def __init__(self, value):
              self.value = value

          @staticmethod
          def get_max_value(x, y):
              return max(x, y)

      # Create an instance of MyClass
      obj = MyClass(10)

      print(MyClass.get_max_value(20, 30))

      print(obj.get_max_value(20, 30))

      class magic:
          def __init__(self):
              self.f1=f
             # def __super().__()

              def use(magic):
                  print("use it")
