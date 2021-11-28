"""


sort():
--------


---->The sort() method sorts the elements of a given in a specific ascending or descending order.

Syntax : list.sort(key=..., reverse=...)

-->Alternatively, you can also use Python's built-in sorted() function for the same purpose.

sorted(list, key=..., reverse=...)

-->The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the original list and returns the sorted list.

-->By default, sort(), sorted() doesn't require any extra parameters. However, it has two optional parameters:

reverse - If True, the sorted list is reversed (or sorted in Descending order)
key - function that serves as a key for the sort comparison

-->The sort() method doesn't return any value. Rather, it changes the original list. If you want a function to return the sorted list rather than change the original list, use sorted().
example: by
default
sorts
the
numbers in ascending
order
--------
list1 = [1, 10, 0.5, 11, 1, 8, 1, 20]
list1.sort()
print(list1)
output:
-------
[0.5, 1, 1, 1, 8, 10, 11, 20]

example: use keyword argument reverse = True sorts the list in the descending order
--------
list1 = [1, 10, 0.5, 11, 1, 8, 1, 20]
list1.sort(reverse=True)
print(list1)
output:
-------
[20, 11, 10, 8, 1, 1, 1, 0.5]

example: by default sorts the string in the alphabetical order
--------
list1 = ['b', 'c', 'a', 'h', 'e', 'aa']
list1.sort()
print(list1)
output:
-------
['a', 'aa', 'b', 'c', 'e', 'h']

example: we can't give values of different type to the sort() method
--------
list1 = ['b', 'c', 'a', 'h', 'e', 'aa', 3, 2, 1]
list1.sort()
print(list1)
output:
-------
Traceback(most recent call last):
File "C:\Users\this\Desktop\sample1.py", line 2, in < module > list1.sort()
TypeError: '<' not supported between instances of 'int' and 'str'

example: I want to sort the list of strings by length
--------
list1 = ['hi', 'how are you', 'python', 'program']
list1.sort(key=len)
print('new list is :', list1)
output:
-------
new
list is: ['hi', 'python', 'program', 'how are you']

-->here key any which is going to get the length of the each elements. then sort() will sort them accordingly.Instread
that there is another way to achieve same thing. see below

example:
--------
list1 = ['hi', 'how are you', 'python', 'program']


def func(n):
    return len(n)


list1.sort(key=func)
print('new list is :', list1)
output:
-------
new list is: ['hi', 'python', 'program', 'how are you']

-->Here when list1.sort(key=func) is executed, each element in the list1 is passed to func(n) as the argument, then the func(n)
returns the length of that list element. so for each and every value in the list, the func(n) is execute.when all the lengths are returned, the sort will sorted them based on length.

-->we can also use the lambda function here like key = lambda x: x, see below
example:
--------
list1 = ['hi', 'how are you', 'python', 'program']
list1.sort(key=lambda x: len(x))
print(list1)
output:
-------
['hi', 'python', 'program', 'how are you']


"""