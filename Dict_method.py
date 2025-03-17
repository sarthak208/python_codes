import pandas
ar2={536:81,154:65.83,64.73:74,'true':"743"}
ep2={657:90,67491:0}
ar2.update(ep2)
print(ar2.update())
ep2.clear()
print(ep2.clear())
ar2.copy()
print(ar2.copy())
seq = ('a', 'b', 'c')
print(dict.fromkeys(seq, None))

d = {1: '001', 2: '010', 3: '011'}

print(d.get(4, "Not found"))


d = {'A': 'Python', 'B': 'Java', 'C': 'C++'}

# using items() to get all key-value pairs
items = d.items()

print(items)

sp2={45:8,100:12000}
print(sp2.keys())
print(ep2)
print(ar2)
print(ep2)
print(ar2)
str={74,82,93}
print(str.pop())

d = {1: '001', 2: '010', 3: '011'}

# Using popitem() to remove and return the last item
res = d.popitem()
print(res)
print(d)
d = {'a': 97, 'b': 98, 'c': 99, 'd': 100} 
# space key added using setdefault() method 
d.setdefault(' ', 32) 
print(d)

group={'disha':64,'srushti':73,'amrita':100}
#s=group.values(64,p)
print(group.values())
