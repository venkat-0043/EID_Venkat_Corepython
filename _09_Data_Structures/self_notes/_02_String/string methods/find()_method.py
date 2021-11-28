
"""


find():
--------

-->The find() method returns the index of the first occurrence of the substring if found. if not found return -1.

syntax : str.find(substing, start, end)

-->The find() method takes maximum of 3 parameters.

substring : it is the substring to be searched in the 'str' string
start and end (optional) : the range str[start:end] within which substring is searched.

-->if the substring exists inside the string, it returns the index of the first occurence of the substring.

example:
--------
string = "Hello world Hello world"
result = string.find('Hello')
print(result)
output:
-------
0

example:
--------
string = "Hello world Hello world"
result = string.find('Hello', 10, 20)
print(result)
output:
-------
12

example: this is same as the example in count() method
--------
string = "Hello world Hello world"
result = string.find('')
print(result)
output:
-------
0

-->Here also the it search for non-space character. so the non-space found at the 0th location.

example:
--------
string = "Hello world Hello world"
result = string.find('hello', 50)
print(result)
output:
-------
-1

-->like count() method, here also We can give the start or the end index which is out of the range. it doesn't return the error. it returns -1.

example:
--------
string = "Hello world Hello world"
result = string.find('Hello', 5, -1)
print(result)
output:
-------
12

-->here we can use the negative index also.

"""