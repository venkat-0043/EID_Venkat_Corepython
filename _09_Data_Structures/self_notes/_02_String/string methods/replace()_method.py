
"""

replace():
----------

-->The replace() method replaces each matching occurrence of the old character/text in the string with the new character/text.

Syntax : str.replace(old, new [, count])
old - old substring you want to replace
new - new substring which will replace the old substring
count (optional) - the number of times you want to replace the old substring with the new substring
Note: If count is not specified, the replace() method replaces all occurrences of the old substring with the new substring.

-->The replace() method returns a copy of the string where the old substring is replaced with the new substring. The original string is unchanged. If the old substring is not found, it returns the copy of the original string.


example:
--------
string = 'python program'
print(string.replace('p', 'P'))
output:
-------
Python Program

-->if I want to replace only first 'p'. then use the count.
example:
--------
string = 'python program'
print(string.replace('p', 'P', 1))
output:
-------
Python program


example: it there is empty string, it returns the empty line.
--------
string = ''
print(string.replace('p', 'P', 1))

"""