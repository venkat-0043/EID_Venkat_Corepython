"""

index():
---------
-->the index() method returns the index of the specified element in the tuple.
syntax : tuple.index(element, start, end)

element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index
Return Value from Tuple index()

-->by default index() method returns the index of the given element first appeared in the tuple. If the element is not found, a ValueError exception is raised.

example:
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
print('1 is at the position : ',tuple1.index(1))
print('2 is at the position : ', tuple1.index(2))
output:
-------
1 is at the position :  0
2 is at the position :  1


example: raises the exception if the index of the element not found.
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
print('index of the element 10 is :', tuple1.index(10))
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    print('index of the element 10 is :', tuple1.index(10))
ValueError: tuple.index(x): x not in tuple


example: use index() with start and end parameters. here we can give uppper limit out of range.
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
print('index of the element 1 is after index 4 is : ', tuple1.index(1, 4, 20))
output:
-------
index of the element 1 is after index 3 is :  5


example: use index() with negative index
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
print('index of the element 1 is at : ', tuple1.index(1, -8, -1))
output:
-------
index of the element 1 is at:  3

"""