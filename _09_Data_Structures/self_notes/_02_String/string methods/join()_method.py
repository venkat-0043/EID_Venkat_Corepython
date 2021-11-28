
"""



join():
-------

-->The join() string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.

Syntax : string.join(iterable)

Some of the example of iterables are:
-------------------------------------
Native data types - List, Tuple, String, Dictionary and Set.
File objects and objects you define with an __iter__() or __getitem()__ method.
Note: The join() method provides a flexible way to create strings from iterable objects. It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.

-->If we want make the string version of comma seperated values from our list. we use the method join().
join() method returns the value of str data type, split() method returns the value in the list format. The join() method takes only one argument either the single strig value or the list of string.
example:
--------
sample = ['apple','mango','cherry']
sample1 = ' , '.join(sample)#this means all the elements will be joined by putting comma in between them
print(sample1)
new_sample = sample1.split(' , ') #this method removes the comma seperation and forms the new list.
print(new_sample)
output:
-------
apple , mango , cherry
['apple', 'mango', 'cherry']


example:
--------
list1 = [ 'hello', 'world', 'python']
result = '-'.join(list1)
print(result)
output:
-------
hello-world-python

-->here I mentioned the string seperator as '-'. it join all the elements in the list by putting the '-' between them. we call '-' as the string seperator. in that single quotes, we can mention any other characters or any symbols.


example : passing the other data types to the join return the error.
---------
list1 = [ 'hello', 'world', 'python', 1,2]
result = '-'.join(list1)
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result = '-'.join(list1)
TypeError: sequence item 3: expected str instance, int found


example: but we can give only tuple, but they should  contain the string data.
--------
list1 = [ 'hello', 'world', 'python', ('hello')]
result = '-'.join(list1)
print(result)
output:
-------
hello-world-python-hello


example: we can't the data type other than tuple()
--------
list1 = [ 'hello', 'world', 'python', ['list'], {'set'}, {'a' : 'apple'}]
result = '-'.join(list1)
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result = '-'.join(list1)
TypeError: sequence item 3: expected str instance, list found


example : .join() with tuples
---------
tuple = ('a', 'b', 'c')
result = '-'.join(tuple)
print(result)
output:
-------
a-b-c


example : in the string seperator ' ', we can give another string also
---------
string1  = 'abc'
list1 = ['1', '2', '3']
result = string1.join(list1)
print(result)
output:
-------
1abc2abc3


"""
