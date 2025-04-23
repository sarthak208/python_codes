import functools

def square(x):
    x = 54
    return x


x = {73, 92, 203, 1000}
ans = map(square, x)
print(list(ans))
a = [72, 9.85, 92, 543]


import functools

# Define a list of numbers
numbers = [1, 2, 3, 4]

# Use reduce to compute the product of list elements
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)

# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))

for numbers in numbers:
 if numbers % 2==0:
        break
 else:
      break

if  numbers %2==0: print("value")
else:print("other value")

try:
    print("choose the local number")

except numbers as x:
    print("othervalue")

finally:
    print("nothing value")

while numbers%2==0:
    print("enter sol value")

x='''entertevalueof  officer rank  person'''
num=input("enter the value of  x ")
print(x)
print(f"x{3}")
