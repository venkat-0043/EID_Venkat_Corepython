

"""

isdigit():
----------

-->The isdigit() method returns True if all characters in a string are digits. If not, it returns False.

Syntax : string.isdigit()

The isdigit() doesn't take any parameters. this method returns True if all characters in the string are digits. False if at least one character is not a digit.

example:
--------
string = '10123'
print(string.isdigit())
output:
-------
True


example:
--------
string = '10abc'
print(string.isdigit())
output:
-------
False


example: we can't float number like '10.5', because '.' is considered as the different character.
--------
string = '10.55'
print(string.isdigit())
output:
-------
False

-->A digit is a character that has property value:

Numeric_Type = Digit
Numeric_Type = Decimal

"""