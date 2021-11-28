
"""

insert():
---------

-->the insert() method inserts an elements to the list at the specified index. The insert() is same as the append(). but for insert() we need to mention the index position, at which we want to insert.

Syntax : list.insert(i, elem)
Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.
The insert() method takes two parameters:

index - the index where the element needs to be inserted
element - this is the element to be inserted in the list

example:
--------
list1 = [1,2,3,4]
list1.insert(2, 2.5)
print(list1)
output:
-------
[1, 2, 2.5, 3, 4]
-->Here we gave the positive index, so 2.5 will be added at the position 2, and elements after the 2nd position will be right shifted by one position.


example:
--------
list1 = [1,2,3,4]
list1.insert(10, 2.5)
print(list1)
output:
-------
[1, 2, 3, 4, 2.5]

-->here I passed the index position as 10, which is out of range. at that time python add the element at the end of the list.

example: using the negative index
--------
list1 = [1,2,3,4]
list1.insert(-2, 2.5)
print(list1)
output:
-------
[1, 2, 2.5, 3, 4]
-->here we gave the negative index. so element will be added at the -2 position, the previous value at the -2 position which is 3, after that 4, all are shifted to right by 1 position.


example:
--------
list1 = [1,2,3,4]
list2 = (5,6,7)
list1.insert(-1, list2)
print(list1)
output:
-------
[1, 2, 3, [5, 6, 7], 4]
-->the insert() works same like append(), if we add the tuple, list, set, dict. they are added with the same structure unchanged.


example: what if don't mention the index position
--------
list1 = [1,2,3,4]
list2 = {'a' : 'apple'}
list1.insert(list2)
print(list1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 3, in <module>
    list1.insert(list2)
TypeError: insert expected 2 arguments, got 1


"""