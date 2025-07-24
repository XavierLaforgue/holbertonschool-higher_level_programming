![Python's Mutable vs Immutable Types: What's the Difference?](images/RelPython_MutableInmutableObjectDifferences.png)

*Image source: [Python's Mutable vs Immutable Types: What's the
Difference?](https://realpython.com/python-mutable-vs-immutable-types/)*

# 🔍 Python3: Mutable, Immutable... Everything is an Object!

Python is considered to be a good starting point to learn programming
due to its readability, relative simplicity, and adaptability via its
many freely available packages/modules.
In Python, **everything is an object**.
Basic datatypes &mdash;such as *integers*, *floats*, *characters*/*strings*, *lists*&mdash;
even *functions* and *modules* are all *objects* in Python.
This is a key fact that needs to be understood to master the language
and to take full advantage of its most powerful features.

An important distinction between objects is that of mutability.
In Python, one may obtain different results when performing a certain
operation on a **mutable** or **immutable** object.
This concept is crucial for writing efficient and bug-free Python code.

## 🆔 `id` and `type`

Every object in Python has:

- a unique identity in memory: `id()`, and 
- a specific type (the class to which the object belongs): `type()`.

These functions are fundamental tools that serve to inspect any object,
determine which class it is instance of and to differentiate one object
from another unambiguously.

```python
a = 256
b = int("256")
print(a == b) 		 # True:  Same value.
print(id(a) == id(b))# True: Same id! Python reuses small (-5 <= int <= 256) integers 
print(a is b)  		 # True: same object. Stored in memory only once.
print(type(a))       # <class 'int'>
print(type(b))       # <class 'int'>

a = 257
b = int("257")
print(a == b)  		 # True:  Same value.
print(id(a) == id(b))# False: Different id! 
print(a is b)  		 # False: different objects. Stored in memory as two independent objects.
print(type(a)) 		 # <class 'int'>
print(type(b))       # <class 'int'>

c = [1, 2, 3]
print(id(c))         # Different from others
print(type(c))       # <class 'list'>

d = [1, 2, 3]
print(id(d))         # Different from others, including the seemingly identical list 'c'
print(type(d))       # <class 'list'>

print(id(d[0]) == id(c[0]))# True: same object 'int' of value '1' referred by the first element of both lists
```
As shown, the operator `is` serves to evaluates equality of identities.
We also see that even if two variables have the same value, they may or may not refer to the same object.
```python
x = "hello"
y = "hello"
print(x is y)  # True: same object, string 'interning'

x = [1, 2]
y = [1, 2]
print(x is y)  # False: two different lists
```
*Interning* refers to an optimization technique where Python stores certain
immutable objects in memory to be used by possibly multiple references to the
same value.
This serves to save space and speed-up comparisons.

## 🔄 Mutable Objects

Mutable objects can be modified in-place, i.e., their state (contained data)
can be modified after creation.

Some examples of mutable objects are: `list`, `dict`, `set`, and most class instances.

```python
my_list = [1, 2, 3]
print(id(my_list))   # ID before modification

my_list.append(4)
print(my_list)       # [1, 2, 3, 4]
print(id(my_list))   # Same ID: modified in-place ---at the same memory location (or at least guarding the same object reference)---
```
Having multiple references to the same objects in memory can lead to
unexpected effects:
```python
a = [10, 20]
b = a     # Both point to the same list
b.append(30)
print(a)  # [10, 20, 30]: surprise 😮!
```
The `+` operator is not equivalent to the `append` method.
While `b.append(30)` adds the element `30` to the end of the list `b`, 
`b+[30]` concatenates the list `b` with the list `[30]` thus producing a new
list object.

## 🔒 Immutable Objects
Immutable objects cannot be changed in-place, their state (the data they
reference) can not be changed.

Some examples of immutable objects are: `int`, `float`, `bool`, `str`, and `tuple`.
```python
x = 10
print(id(x))         # ID before

x += 1               # Creates a new 'int' object
print(x)             # 11
print(id(x))         # New ID!
```
Even operations that seem to modify immutable objects, are really just
creating new instances of objects of the same class:
```python
s = "hello"
print(id(s))

s += " world"
print(s)             # "hello world"
print(id(s))         # New ID!
```
The above, as mentioned in the case of lists, is also an example of
concatenation and the subsequent automatic creation of a new object.

Tuples are immutable, but they can contain mutable items (without restricting their mutability):
```python
t = (1, [2, 3])
t[1].append(4)       # Legal: modifies the list inside the tuple
print(t)             # (1, [2, 3, 4])

u = t[1] + [5]		 # Legal: this creates a new list concatenating the one in the tuple and the list [5]
print(u)             # [2, 3, 4, 5]

t[0] = 2 			 # Illegal: this would change the first element of the tuple
t[1] = t[1] + [5]	 # Illegal: this would modify the tuple by changing the list object it contains
```
## 🤔 Why Does It Matter?
Python treats mutable and immutable objects differently when it comes
to assignment, copying, and function calls.

### Assignment:
When two variables refer to the same object, and one of them demands a
modification of the object, the results will vary depending on the
mutability of the object:
- If the object is mutable, the object will modified and both
variables will refer to the same modified object.
- If the object is immutable, the variable demanding a modification on
  the object will instead be reassigned to the new object resulting of
  the modification, while the other variable will continue to reference
  to the first/original object.
```python
# Immutable
a = 5
b = a
print(a is b) 		 # True: 'a' and 'b' refer to the same object
b += 1
print(a, b)          # 5, 6: 'b' is a new object
print(a is b)    	 # False: 'b' refers now to a different object

# Mutable
list1 = [1, 2]
list2 = list1
print(list1 is list2)# True: refer to the same list
list2.append(3)
print(list1, list2)  # [1, 2, 3], [1, 2, 3]: same object
print(list1 is list2)# True: still refer to the same list
```
### Copying:
Creating copies of mutable objects can help avoid the side effect of
object changes affecting all variables that reference it, this can be
performed using either shallow or deep copy functionalities:
- Shallow copy creates a new object containing the same elements as the
  original.
- Deep copy creates a new object containing copies of its containing
  elements.
Creating copies of immutable objects is normally unncessary since
attempting changes on a variable will only change the reference from
one object to another without affecting other variables that referenced
the original object.
```python
import copy

original = [1, 2, 3]
shallow = original[:]      # shallow copy of the list [also with list(original)]
deep = copy.deepcopy(original)# deepcopy of the original list
shallow.append(4)
deep.append(5)
print(original)            # [1, 2, 3]: Unchanged
print(shallow)             # [1, 2, 3, 4]: Shallow was modified
print(deep)                # [1, 2, 3, 5]Deep was modified

original = [1, 2, 3, [4, 5]]
shallow = original[:]      # shallow copy of the list containing the same nested list object as the original
deep = copy.deepcopy(original)# deepcopy of the original list (makes copy fo nested list)
shallow[3].append(6)
shallow.append(7)
deep[3].append(8)
deep.append(9)
print(original)            # [1, 2, 3, [4, 5, 6]]: Unchanged except for the nested list which was changed with shallow
print(shallow)             # [1, 2, 3, [4, 5, 6], 7]: Shallow was modified, different elements except for the nested list which is also referenced by original
print(deep)                # [1, 2, 3, [4, 5, 8], 9]: Deep was modified, all new objects
```
## 📦 Function Arguments: Passing Mutable and Immutable Objects
Function arguments in Python are passed by object reference.
This causes objects to behave differently depending on if they are
mutable or immutable.

As they are passed by reference to functions, a mutable object that is
modified inside the function will also be modified outside of it (the
reference in the global and function scopes point to the same object &mdash;
and object may be modified in memory during the function call).
On the other hand, when a function attempts to modified a immutable
object, it will only change the internal (aliased) reference to a
different/new object while leaving the external reference unchanged.
```python
# Immutable case:
def modify(n):
    n += 1
    print("Inside:", n)

x = 10
modify(x)
print("Outside:", x)  # Unchanged: 10

# Mutable case:
def mutate(lst):
    lst.append(99)
    print("Inside:", lst)

my_list = [1, 2]
mutate(my_list)
print("Outside:", my_list)  # Changed: [1, 2, 99]
```
Rebinding inside function doesn't affect outer variable (this is valid
to both mutable and immutable objects):
```python
def rebind(l):
    l = [100]        # New local reference
    print("Inside:", l)

my_list = [1, 2]
rebind(my_list)
print("Outside:", my_list)  # Still [1, 2]
```
A way to avoid modifications on mutable object during function calls is
to explicitly make copies of them in the function:
```python
def safe_modify(lst):
    lst = lst.copy()
    lst.append(42)
    print("Inside:", lst)

original = [10, 20]
safe_modify(original)
print("Outside:", original)  # Unchanged: [10, 20]
```
## ✅ Final Takeaways

Everything in Python is an object.

Understanding the difference between how mutable and immutable objects
are treated in Python can
help avoid undesired behavior in programs.

One can use `id()` and `type()` to inspect objects and determine when
variables reference the same or different objects even when their
contents seem identical.

One must be cautious when sharing references to mutable objects.

Python passes arguments by object reference.

Defensive copying can prevent subtle bugs.
