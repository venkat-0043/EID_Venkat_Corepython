
"""

index():
---------

-->The index() method returns the index of the specified element in the list. The index() method only returns the first occurrence of the matching element.

Syntax : list.index(element, start, end)

element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index

-->The index() method returns the index of the given element in the list.If the element is not found, a ValueError exception is raised. The index() method only returns the first occurrence of the matching element.

example:
--------
list1 = ['a', 'b', 'c', 'a', 'd']
result = list1.index('a')
print(result)
output:
-------
0

example:
--------
list1 = ['a', 'b', 'c', 'a', 'd']
result = list1.index('a', 1, 10)
print(result)
output:
-------
3
-->here I give the start = 1, end = 10 which is out of range. it don't give the error, it just assumes till last value.


example: we can also give the negative start and end index
--------
list1 = ['a', 'b', 'c', 'a', 'd']
result = list1.index('a', -3, -1) #we can also write like list1.index('a', -3)
print(result)
output:
-------
3
-->while giving the negative indexing the start value < upper value.


example: what if value not in the list
--------
list1 = ['a', 'b', 'c', 'a', 'd']
result = list1.index('e')
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result = list1.index('e')
ValueError: 'e' is not in list

"""