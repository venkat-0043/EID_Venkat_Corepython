
"""


count():
---------

-->the count() method returns the number of occurances of a substring in the given string.
syntax : string.count(substring, start index , end index )

-->the count() method only requires a single parameter for execution. However, it also has 2 optional parameters :

substring - string whose count is to be found
start(optional) - starting index within the string where search starts
end(optional) - ending index within the string where search ends.
Note : in python index starts at 0 not 1.

example:
--------
string = "this is python"
result = string.count("is")
print(result)

output:
-------
2
-->here the the result is 2, because 'is' is found in the word 'this', and there is another 'is'.

example:
--------
string = "this is python"
result = string.count("is", 5 )
print(result)

output:
-------
1
-->start and end index are optional, so I can give just start point.

example:THIS IS DIFFERENT SCENARIO
--------
string = "this is python"
result = string.count("")
print(result)
output:
-------
15

"""