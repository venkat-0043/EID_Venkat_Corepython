
"""

list slicing and indixing:
--------------------------

-->A list is an ordered and mutable python container which allows the duplicate values. In short, a list is a ordred collection of arbitrary objects. Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]).

-->The important characteristics of Python lists are as follows:

1)Lists are ordered.
2)Lists can contain any arbitrary objects.
3)List elements can be accessed by index.
4)Lists can be nested to arbitrary depth.
5)Lists are mutable.
6)Lists are dynamic.

-->lists are the sequences. here are certain things you can do with all sequence types.
These Sequence operations include
1.  indexing
2.	slicing
3.	adding
4.	multiplying and
5.	checking for membership.

In addition, Python has built-in functions for
6.	len()        : finding the length of a sequence
7.	max()      : for finding its largest element
8.	min()       : for finding its smallest elements.

1)indexing:
-----------
-->The individual elements in the list can be accessed using an index in square brackets. list indexing is zero-based. we can use the negative indexing also.

example:
--------
ist1 = [1, 2, 3, 'hello']
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[-1])

output:
-------
1
2
3
hello


-->if we try to access the element in the list with the index out of the lenth of the list, it raises the exception.
example:
--------
list1 = [1, 2, 3, 'hello']
print(list1[10])
print(list1[-10])

output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    print(list1[10])
IndexError: list index out of range


2)Slicing:
----------
-->Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists. You can also use them to modify or delete the items of mutable sequences such as lists. Slices can also be applied on third-party objects like NumPy arrays, as well as Pandas series and data frames.

-->In a list, the expression list[m:n] returns the portion of a from index m to, but not including, index n.

example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[0 : 3])

output:
-------
['hello', 'world', 'python']

-->Here the upper bound 3 is excluded.

-->in slicing we can use the negative indexing
example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[-3:-1])
output:
-------
['world', 'python']

-->we can't start the slicing with -1. it only prints the last element.
example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[-1 : ])
output:
-------
['program']

example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[-1 : -5])
output:
-------
[]
-->The reason it prints the empty list is we started with -1 and end with -5. normally in the slicing the increment is done by +1. so going from -1 to -5 with a positive increment in not possible. To achieve that we have to explicitly mention the step value as -1. see below
example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[-1 : -5 : -1])
output:
-------
['program', 'python', 'world', 'hello']


-->Omitting the first index starts the slice at the beginning of the list, and omitting the second index extends the slice to the end of the list.

example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[: 3])
print(list1[1 : ])
print(list1[ : ])
output:
-------
['hello', 'world', 'python']
['world', 'python', 'program']
['hello', 'world', 'python', 'program']

-->In slicing you can mention the index which is out of range also. it don't give the error.
example:
--------
list1 = ['hello', 'world', 'python', 'program']
print(list1[: 10])
print(list1[ 10: ])
output:
-------
['hello', 'world', 'python', 'program']
[]


-->we can also mention the stride or step value either positive or negative value :
example:
--------
list1 = ['hello', 'world', 'python', 'program', 123]
print(list1[0 : 4 : 2])
print(list1[-1 : -6 : -2])
output:
-------
['hello', 'python']
[123, 'python', 'hello']


-->printing the reverse of the list
example:
--------
list1 = ['hello', 'world', 'python', 'program', 123]
print(list1[: : -1])
output:
-------
[123, 'program', 'python', 'world', 'hello']


-->The [:] syntax works for lists. However, there is an important difference between how this operation works with a list and how it works with a string.

If s is a string, s[:] returns a reference to the same object:

>>> s = 'foobar'
>>> s[:]
'foobar'
>>> s[:] is s
True

-->Conversely, if a is a list, a[:] returns a new object that is a copy of a:

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a[:]
['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a[:] is a
False

"""