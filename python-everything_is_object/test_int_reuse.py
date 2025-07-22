#!/usr/bin/python3
a = 256
b = int("256")
print(a == b)
print(id(a) == id(b)) 
print(a is b)  # Usually False
print(type(a))

a = 257
b = int("257")
print(a == b)
print(id(a) == id(b)) 
print(a is b)  # Usually False
print(type(a))

print("---")

c = [1, 2, 3]
print(id(c))         # Different from others
print(type(c))       # <class 'list'>

d = [1, 2, 3]
print(id(d))         # Different from others
print(type(d))       # <class 'list'>

print(id(d[0]) == id(c[0]))

t = (1, [2, 3])
t[1].append(4)       # Legal: modifies the list inside the tuple
print(t)             # (1, [2, 3, 4])

u = t[1] + [5]		 # Legal: this creates a new list concatenating the one in the tuple and the list [5]
print(u)

a = [1, 2, 3]
b = list(a)
a.append(4)
print(a)
print(b)
print(a is b)

