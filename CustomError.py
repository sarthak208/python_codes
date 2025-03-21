import math
#def_error(x,y):
x=input("enter value of x is 3 and y is 7")
print(x)
print(y)
if(x<= 3 and y>=7):
raise arthimetic error("value shouled be 3 and 7")
print(raise arthimetic error)
else:
    print("the value will be another block")
    
try:
    print("enter the value between both")
    
except logical error: 
    raise logical error("value shouled be 3 and 7")
    
else:
    print("nothing value will excuare")

finally:
    print("value will  finalize")
    
    x=3
    y=7
  for x in x:
      if(x==3)
        break
      for y in y:
          if(y==7)
          break
      print(x)
      print(y)

class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class InvalidInputError(CustomError):
    """Raised when the input is invalid"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Example usage
def divide_numbers(a, b):
    if b == 0:
        raise InvalidInputError("Cannot divide by zero!")
    return a / b

try:
    result = divide_numbers(10, 0)
except InvalidInputError as e:
    print(f"Error: (e))
