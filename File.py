f=open("script.py","r")
with open("script.py","r") as f:
f.tell(20)

s = open("script.py", "rw")
with open("script.py","rw") as s:
s.readline(20)

l = open("script.py", "w")
with open("script.py","w") as l:
l.seek(20)



print(f.tell())
print(s.readline())
print(l.seek())

f.close()
