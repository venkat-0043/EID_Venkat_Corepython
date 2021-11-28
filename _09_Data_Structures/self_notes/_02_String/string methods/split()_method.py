
"""

split():
--------

-->The split() method breaks up a string at the specified separator and returns a list of strings. be default it splits by space ' '.

Syntax : str.split(separator, maxsplit)

separator (optional)- Delimiter at which splits occur. If not provided, the string is splitted at whitespaces.
maxsplit (optional) - Maximum number of splits. If not provided, there is no limit on the number of splits.

Note : The split() method returns a list of strings.

example: by default it splits based on space ' '.
--------
string = 'this is python program'
print(string.split())
output:
-------
['this', 'is', 'python', 'program']

example:
--------
string = 'this is python program'
print(string.split(' ', 2))
output:
--------
['this', 'is', 'python program']
-->here i mentioned the max split is 2. so it stops splitting after 2 splits.


example : we can use the string seperator any character
---------
string = 'this is python program'
print(string.split('i', 2))
output:
-------
['th', 's ', 's python program']


example: it the seperator string is not found, it returns the entire string as the list element.
--------
string = 'this is python program'
print(string.split('z', 2))
output:
-------
['this is python program']

"""