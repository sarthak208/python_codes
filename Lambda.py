import math
import hashlib
value= lambda x:x*3
print(value(3))

x1=lambda x2,x3,x4:(65+728+10)/3
print(x1)

for x1 in range(6):
    print(x1)


try:
    print("using x vlue")

except value as x:
   print("other value")

finally:
     print("noone use")

d='''the value of given term it  is satisfivally'''
print(f"the valueof givven {d}")

f='''intial value can ve derive'''
print(f.__doc__)
a={"indian legend army"}
input("enter thevalue of a")
print(a)

for a in a:
   print(a)

   if f==a:
      break

   else:
       print("other value given")

if f==a: print("entr thatvalue")

def os(f=6):
    print("the value of f")
    os(f)
