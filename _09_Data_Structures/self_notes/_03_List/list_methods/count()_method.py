"""

count():
--------

-->The count() method returns the number of times the specified element appears in the list.

Syntax : list.count(element)
element - the element to be counted

example:
--------
list1 = ['a', 'b', 'c', 'a', 'd']
print(list1.count('a'))
output:
-------
2

example:
--------
list1 = ['a', 'b', 'c', 'a', 'd']
print(list1.count('e'))
output:
-------
0
-->if the element not found in the list, it return 0, not raises exception.

-->we can also pass the different data type values.
example:
--------
list1 = [[1,2], 3, 4, [1,2], (1,2), (1,2)]
print(list1.count([1,2]))
output:
-------
2

example:
--------
list1 = [[1,2], 3, 4, [1,2], {'a' : 'apple'}]
print(list1.count({'a' : 'apple'}))
output:
-------
1

"""
