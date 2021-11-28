
"""

min() and max():
----------------
-->max() function is used to compute the maximum of the values passed in its argument. min() returns the minimum of the values passed to it. but they only accept values of the same type. like either list, string, tuple etc.

example:
--------
list1 = [1, 2, 3, 4, 10, 1, 5]
print(max(list1))
print(min(list1))
output:
-------
10
1

example: for alphabets, it check ASCII values
--------
list1 = ['l', 'm', 'list', 't', 'a', 'B']
print(max(list1))
print(min(list1))
output:
-------
t
B

example: we can't pass empty sequence to the max() and min().
--------
list1 = []
print(max(list1))
print(min(list1))
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    print(max(list1))
ValueError: max() arg is an empty sequence

"""