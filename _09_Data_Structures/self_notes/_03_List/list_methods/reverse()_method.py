"""

reverse():
-----------
-->the reverse() method reverses the elements of the list.

Syntax : list.reverse()

-->The reverse() method doesn't take any arguments. The reverse() method doesn't return any value. It updates the existing(original) list.

example:
--------
list1 = [1, 10, 0.5, 11 , 2, 8]
print(list1.reverse())
print(list1)
output:
-------
None
[8, 2, 11, 0.5, 10, 1]
-->the return value in None, the reason it updates the original list.


example:
--------
list1 = [1, 10, 0.5, 11 , 2, 8, 'hello', 20, 'world']
print(list1.reverse())
print(list1)
output:
-------
None
['world', 20, 'hello', 8, 2, 11, 0.5, 10, 1]


example:
--------
list1 = []
print(list1.reverse())
print(list1)
output:
-------
None
[]


example : accessing the elements in the reverse order
---------
list1 = [1, 10, 0.5, 11 , 2, 8, 'hello', 20, 'world']
for i in list1.reverse():
    print(i)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    for i in list1.reverse():
TypeError: 'NoneType' object is not iterable

-->this raises the error, because the reverse() operation returns None. you can't perform operation against None type value.
-->To access the elements in the reverse order use the method reversed(). see below :

example:using the method REVERSED()
--------
list1 = [1, 10, 0.5, 11 , 2, 8, 'hello', 20, 'world']
for i in reversed(list1):
    print(i)
output:
-------
world
20
hello
8
2
11
0.5
10
1

"""