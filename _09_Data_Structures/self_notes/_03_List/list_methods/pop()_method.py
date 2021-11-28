"""

pop():
------
-->the pop() method removes the item at the given index from the list and returns the removed item.
Syntax : list.pop(index)

-->The pop() method takes a single argument (index). The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
-->If the index passed to the method is not in range, it throws IndexError: pop index out of range exception. The pop() method returns the item present at the given index. This item is also removed from the list.

example:
--------
list1 = [1, 10, 0.5, 11 , 2, 8, 'hello', 20, 'world']
removed_item = list1.pop() #by default index = -1
print('removed item is : ' ,  removed_item)
print('new list is :', list1)
output:
-------
removed item is :  world
new list is : [1, 10, 0.5, 11, 2, 8, 'hello', 20]


example: use the negative index
--------
list1 = [1, 10, 0.5, 11 , 2, 8, 'hello', 20, 'world']
removed_item = list1.pop(-2)
print('removed item is : ' ,  removed_item)
print('new list is :', list1)
output:
-------
removed item is :  20
new list is : [1, 10, 0.5, 11, 2, 8, 'hello', 'world']


example: try with index out of range
--------
list1 = [1, 10, 0.5, 11 , 2, 8, 2, 'hello', 20, 'world']
removed_item = list1.pop(20)
print('new list is :', list1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    removed_item = list1.pop(20)
IndexError: pop index out of range


"""