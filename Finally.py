def_math(a,b):
a=15
a=input("enter value of a")
print("the value of a is")
b=5
b=input("enter value of b")
print("the value of b is")
try:
b=int(input("enter a num"))
result=15/b
except ZeroDivisionError:
print("you cannot divide by zero")
except ValueError:
print("invallid input num")
except exception as e:
print(f"an error occured(e)")
else:
print("you cannot find anthing")
finally:
print("only b will excuate")
def_result(c=3):
'''the value of c is 3'''
c=input("the value of c")
print(c.__docstring__)
