# Python3: Mutable, Immutable… Everything Is an Object!
## Introduction

Python is a beautifully simple language on the surface, but beneath that simplicity lies a powerful object model that affects everything you do:
- variables
- data structures
- function calls
- memory behavior
One of the first profound realizations you encounter when really learning Python is this: **everything in Python is an object**.
Understanding what objects are, how they behave, and how Python manages them is essential for writing efficient, bug-free code.
This article summarizes everything I learned during the project *“Python - Everything is object”*, illustrated with examples that reveal the sometimes surprising behavior of Python variables.

---

## id and type
Every value in Python is an object, and every object has:
- a **type** → determines what kind of object it is,
- an **id** → its unique identity (its memory address in CPython).

Example:
```python
a = 42
print(type(a))   # <class 'int'>
print(id(a))     # e.g., 140032485120784
```

Two variables can have:
- the **same value**
- the **same type**
- but **not the same identity**

Example:
```python
a = 1000
b = 1000

print(a == b)  # True: same value
print(a is b)  # False: different objects
```

---

## Mutable Objects
A **mutable object** can change its value in place without changing its identity.
Lists are the most common example.
```python
l1 = [1, 2, 3]
l2 = l1

l1.append(4)

print(l1)  # [1, 2, 3, 4]
print(l2)  # [1, 2, 3, 4]
print(l1 is l2)  # True
```

When you mutate a list, variables pointing to that list will all “see” the change.
Another example:
```python
a = [1, 2, 3]
print(id(a))         # 14003248723XXX

a += [4]
print(id(a))         # same id!
```
`+=` mutates the list in place.

---

## Immutable Objects
Immutable objects cannot change once created.
Any “modification” creates a **new object** instead of altering the existing one.

Examples:
- `int`
- `float`
- `bool`
- `str`
- `tuple`

```python
a = 10
print(id(a))        # e.g., 140032485120784

a += 1
print(id(a))        # NEW id!
```

Same with strings:
```python
s = "Hello"
print(id(s))

s += "!"
print(id(s))        # different object
```

---

## Why does this matter ?
Because Python treats mutable and immutable types very differently and confusing bugs often come from misunderstanding this behavior.
Example: list concatenation vs append:
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)

print(l2)  # [1, 2, 3, 4]   → mutation
```

But:

```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]

print(l2)  # [1, 2, 3]       → new list created!
```

Here, `l1 + [4]` creates a **new** list — so `l1` no longer points to the same object as `l2`.

---

## How Python passes arguments to functions
Python uses **call-by-object** (also called call-by-sharing).
A function receives a reference to an object, never the actual variable name.

### Immutable argument example
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1
```

`n += 1` creates a new int object, leaving `a` unchanged.

### Mutable argument example
```python
def mutate(l):
    l.append(4)

l1 = [1, 2, 3]
mutate(l1)
print(l1)  # [1, 2, 3, 4]
```

Here the list is mutated in place, so the change persists.

### Reassignment inside a function does NOT affect the outside
```python
def assign_value(l, v):
    l = v   # only changes local reference

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # unchanged
```

---

## Advanced tasks – surprising behaviors
### Small integers and string interning

CPython optimizes memory by **reusing certain immutable** objects, such as:
- small integers (from –5 to 256)
- some strings (interned strings)

Example:
```python
a = 1
b = 1
print(a is b)   # True (small integer caching)
```

But:
```python
a = 1024
b = 1024
print(a is b)   # Often False (no caching)
```

Same with strings:
```python
a = "SCHL"
b = "SCHL"
print(a is b)  # Often True (interning)

del a
del b

c = "SCHL"
# c may or may not be the same object as before
```

---

## Conclusion
Understanding Python’s object model is essential for mastering the language.
Knowing the difference between ***identity***, ***value***, and ***type***, and understanding how ***mutable*** vs ***immutable*** objects behave, helps avoid bugs that confuse even experienced developers.

Most importantly:
- Variables do NOT contain objects—they reference them.
- Mutating a mutable object affects all references to it.
- Reassigning a variable does NOT mutate the object.
- Python functions work with references, but not the variable names.

Mastering these concepts elevates the way you think and code in Python, and prepares you for technical interviews where these topics often appear.
