
"""
-->len() return the length of the object.
example:
--------
tuple1 = (1,2,3,4,5, {'a' : 'apple'}, [1,2])
print(len(tuple1))
output:
-------
7


example:
--------
tuple1 = (1,2,3,4,5, {'a' : 'apple'}, [1,2])
tuple1 = ()
print(len(tuple1))
print(len(tuple()))
output:
-------
0
0


-->min(), max() returns the minimum and maximum values from an object. but the elements should be of same data type. otherwise it raises typeerror.
example:
--------
tuple1 = (1,2,3,4,5)
print(min(tuple1))
print(max(tuple1))
output:
-------
1
5

example:
--------
tuple1 = ('python', 'Python', 'string', 'tuple')
print(min(tuple1))
print(max(tuple1))
output:
-------
Python
tuple

-->for strings it checks ASCII values

"""