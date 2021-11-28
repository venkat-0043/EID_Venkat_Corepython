"""

remove():
---------
-->The remove() method removes the first matching element (which is passed as an argument) from the list.

syntax : list.remove(element)

-->The remove() method takes a single element as an argument and removes it from the list. If the element doesn't exist, it throws ValueError. The remove() doesn't return any value (returns None).

example:
--------
list1 = [1, 10, 0.5, 11 , 1, 8, 1, 'hello', 20, 'world']
removed_item = list1.remove(1)
print('removed item is : ', removed_item)
print('new list is :', list1)
output:
-------
removed item is :  None
new list is : [10, 0.5, 11, 1, 8, 1, 'hello', 20, 'world']


-->In the above it is removing the value at a single place. there still 1 in other places in the list. To remove all the 1's just write the for loop. see below :
example:
--------
list1 = [1, 10, 0.5, 11 , 1, 8, 1, 'hello', 20, 'world']
for i in list1:
    if i == 1:
        list1.remove(i)

print('new list is :', list1)
output:
-------
new list is : [10, 0.5, 11, 8, 'hello', 20, 'world']


example: try to remove the element not in the list using remove(), causes exception
--------
list1 = [1, 10, 0.5, 11 , 1, 8, 1, 'hello', 20, 'world']
list1.remove(30)
print(list1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    list1.remove(30)
ValueError: list.remove(x): x not in list


example: remove() takes atleast one argument
--------
list1 = [1, 10, 0.5, 11 , 1, 8, 1, 'hello', 20, 'world']
list1.remove()
print(list1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    list1.remove()
TypeError: remove() takes exactly one argument (0 given)

"""