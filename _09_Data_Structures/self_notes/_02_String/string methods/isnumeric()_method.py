
"""

isnumeric():
------------

-->Python String isnumeric() method is a built-in method used for string handling. The issnumeric() method returns “True” if all characters in the string are numeric characters, Otherwise, It returns “False”. This function is used to check if the argument contains all numeric characters such as integers, fractions, subscript, superscript, roman numerals, etc.(all written in Unicode).

syntax : string.isnumeric()

Parameters: isnumeric() does not take any parameters

Returns :

True – If all characters in the string are numeric characters.
False – If the string contains 1 or more non-numeric characters.

Errors and Exceptions:

It does not contain any arguments, therefore, it returns an error if a parameter is passed.
Whitespaces are not considered to be numeric, therefore, it returns “False”
Subscript, Superscript, Fractions, Roman numerals (all written in Unicode)are all considered to be numeric, Therefore, it returns “True”

example:
--------
string = '12345'
print(string.isnumeric())
output:
-------
True

example:
--------
string = '12345@python'
print(string.isnumeric())
output:
-------
False


"""