
"""

splitlines():
-------------

-->The splitlines() method splits the string at line breaks and returns a list of lines in the string.

syntax : str.splitlines([keepends])
keepends (optional) - If keepends is provided and True, line breaks are also included in items of the list.
By default, the line breaks are not included.

-->splitlines() returns a list of lines in the string. If there are not line break characters, it returns a list with a single item (a single line).

splitlines() splits on the following line boundaries:

Representation	Description
--------------  ------------
\n							Line Feed
\r							Carriage Return
\r\n						Carriage Return + Line Feed
\v or \x0b			Line Tabulation
\f or \x0c			Form Feed
\x1c						File Separator
\x1d						Group Separator
\x1e						Record Separator
\x85						Next Line (C1 Control Code)
\u2028					Line Separator
\u2029					Paragraph Separator

Example: How splitlines() works?
--------
grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())

Output:
-------
['Milk', 'Chicken', 'Bread', 'Butter']
['Milk\n', 'Chicken\r\n', 'Bread\r', 'Butter']
['Milk Chicken Bread Butter']


"""