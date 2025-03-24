import hashlib
import pandas

# Initializing lists
a = ["Geeks", "for", "Geeks", "reverse", "bayas"]
a[4]=2
b = ["sab", "khelo", "sub"]
b[2]=0

# Iterating list 'a' using enumerate to get both index and element
for i, name in enumerate(a):
    print(f"Index {i}: {name}")
print(list(enumerate(a)))

# Iterating list 'b' using enumerate to get both index and element
for j, name in enumerate(b):
    print(f"Index {j}: {name}")
print(list(enumerate(b)))

# Example of condition (if you want to compare items in a and b lists)
if(a[4] <= b[2]): 
    print("Condition met")

# Using try-except for error handling
try:
    for a[4] in a:
        if(a[4]==b[2]):
            continue
    print("Use [a] only:", a[4])
except:
    for b[2] in b:
        if(b[2]==a[4]):
            continue
        print("Use [b] only:", b[2])

    print("Index out of range, use only [b]")
else:
    print("Successfully used [a]")

finally:
    print("Default case")

# Correct match statement (Python 3.10+ feature)
match a[4]:  # Matching the 5th element of list 'a'
    case "Geeks":
        print("Geeks")
    case "for":
        print("for")
    case "reverse":
        print("reverse")
    case "bayas":
        print("bayas")
    case _:
        print("Nothing matched")

# In case you want to test b[2] as well
match b[2]:  # Matching the 3rd element of list 'b'
    case "sab":
        print("sab")
    case "khelo":
        print("khelo")
    case "sub":
        print("sub")
    case _:
        print("Nothing matched in b")
