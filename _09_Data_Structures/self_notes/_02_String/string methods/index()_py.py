
"""


index():
--------

-->the index() method returns the index of a substring inside the string if found. if the substring is not found, it raises an exception.

syntax : str.index(substring, end, start)

-->The index() method takes 3 paraemeters
substring : substring to be searched in the string
start and end : substring is searched within string[start : end].

-->if substring exists inside the string, it returns the lowest index in the string wher substring is found. otherwise raises exception.

example:
--------
string = 'this is python programming'
result= string.index('is')
print(result)
output:
-------
2

example:
--------
string = 'this is python programming'
result= string.index('is', 4)
print(result)
output:
-------
5

example:
--------
string = 'this is python programming'
result= string.index('is', -30)
print(result)
output:
-------
2

-->Here also we can give the negative indexing

example:
--------
string = 'this is python programming'
result= string.index('was')
print(result)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    result= string.index('was')
ValueError: substring not found


"""