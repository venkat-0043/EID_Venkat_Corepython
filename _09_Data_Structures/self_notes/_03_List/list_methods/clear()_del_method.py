
"""

-->the clear() method remvoes all items from the list.

Syntax : list.clear()

-->The clear() method doesn't take any parameters. The clear() method only empties the given list. It doesn't return any value.

example:
--------
list1 = [1,2,3, [3,4], (5,6),'a']
print(list1.clear())
print(list1)
output:
-------
None
[]
-->here the clear() operation returns None. means it internally delete all the elements, doesn't return deleted elements like pop().


del():
------
-->The del keyword in python is primarily used to delete objects in Python. Since everything in python represents an object in one way or another, The del keyword can also be used to delete a list, slice a list, delete a dictionaries, remove key-value pairs from a dictionary, delete variables, etc.
Syntax: del object_name

example:
--------
list1 = [1,2,3, [3,4], (5,6),'a']
del list1
print(list1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 3, in <module>
    print(list1)
NameError: name 'list1' is not defined

-->here the 'del' deleted the entire list object. if we try to print the list again, it returns the error.
-->using the clear() we can remove all the elements in the list, but using the 'del' we can remove particular portin of elements in the list using the slicing.


example: here the object is not deleted, only elements in that object are deleted.
--------
list1 = [1,2,3, [3,4], (5,6),'a']
del list1[:]
print(list1)
output:
-------
[]

example:
--------
list1 = [1,2,3, [3,4], (5,6),'a']
del list1[1 : 3]
print(list1)
output:
-------
[1, [3, 4], (5, 6), 'a']


example: using the negative indexing
--------
list1 = [1,2,3, [3,4], (5,6),'a']
del list1[-5 : -1]
print(list1)
solution:
---------
[1, 'a']

example: use the step value, while using the indexing
--------
list1 = [1,2,3, [3,4], (5,6),'a']
del list1[-1 : -5 : -1]
print(list1)
output:
-------
[1, 2]

"""