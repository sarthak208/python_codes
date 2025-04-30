# A simple decorator function
import functools
import math

from datetime import time

x = time(hour=15)
print(x)
hour=input("enter thevalueof hour")
print(hour)
hour=24
try:
 print("enter thevalue of  hours")

except:
    print("enter the alue of other")

finally:
    print("notheruse")

if(x==15):print("value will be correct")
elseif: print("use otherwords")
y=76
dict={x:15,y:76}
print(dict)


# cook your dish here
def math(v):
    v = 7834


if __name__ == "main":
    print("enter the  value of name")

else:
    "__name__ ==main"
print("enter the  value of name")
elseif: "__name__==main"
print("enter the  value of name")
for v in range(7834):
    print(v)
while(v==7834):
    print(v)
class dare:
     j="super"
     k="kammal"
def __init__(self,j,k):
    self.j=j
    self.k=k

dare=("solider","farmer")
print(dare)
print(dare)


def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")

    return wrapper


# Applying the decorator to a function
@decorator
def greet():
    print("Hello, World!")


greet()# A simple decorator function
def decorator(func):

    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()
def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")

greet()
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name)

while(1==0):
    print("function will strats")

if(1==obj):
    breakpoint()
    print("obj willshown")

elif(0==obj):
    breakpoint()
    print("obj will  not shown")

else:
    breakpoint()
    print("obj will be othrt shown")

for func in range(5):
    for func in  func:
        print(func)
    print(func)
