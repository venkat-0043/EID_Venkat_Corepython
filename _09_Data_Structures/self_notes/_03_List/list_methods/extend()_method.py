
"""

extend():
---------

-->the extend() method adds all the elements of an iterable like list, tuple, string, dict, set to the end of the list.
syntax :list1.extend(iterable)
-->The extend() method takes an iterable such as list, tuple, string etc. The extend() method modifies the original list. It doesn't return any value.

example: adding a list
--------
list1 = [1,2,3,4]
list2 = [5,6,7]
list1.extend(list2)
print(list1)
output:
-------
[1, 2, 3, 4, 5, 6, 7]
-->here when we add the list, the list values are added, not added as a sublist.

example: adding a tuple
---------
list1 = [1,2,3,4]
list2 = (5,6,7)
list1.extend(list2)
print(list1)
output:
-------
[1, 2, 3, 4, 5, 6, 7]

exmaple : adding the set
---------
list1 = [1,2,3,4]
list2 = {'hello', 10, 20}
list1.extend(list2)
print(list1)
output:
-------
[1, 2, 3, 4, 10, 'hello', 20]


example:adding the dictionary
--------
list1 = [1,2,3,4]
list2 = {'a' : 'apple'}
list1.extend(list2)
print(list1)
output:
-------
[1, 2, 3, 4, 'a']
-->here only dictionary keys are added. to add the values also we can't write like {{'a' : 'apple'}}. this returns the error. we can write like ({'a' : 'apple'}), here same key is added. to achieve the write the dictionary in the list like [{'a' : 'appel'}]. see below
example:
--------
list1 = [1,2,3,4]
list2 = [{'a' : 'apple'}]
list1.extend(list2)
print(list1)
output:
-------
[1, 2, 3, 4, {'a': 'apple'}]


example: we can't directly pass a single number to the extend() method. cause int is not iterable.
--------
list1 = [1,2,3,4]
list2 = 10
list1.extend(list2)
print(list1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 3, in <module>
    list1.extend(list2)
TypeError: 'int' object is not iterable

"""