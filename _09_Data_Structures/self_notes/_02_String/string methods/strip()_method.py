
"""

strip():
---------

-->The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).

Syntax : string.strip([chars])
chars (optional) - a string specifying the set of characters to be removed from the left and right part of the string.

-->The strip() method removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).
Note: If the chars argument is not provided, all leading and trailing whitespaces are removed from the string. strip() returns a copy of the string with both leading and trailing characters stripped.

-->When the character of the string in the left mismatches with all the characters in the chars argument, it stops removing the leading characters.
Similarly, when the character of the string in the right mismatches with all the characters in the chars argument, it stops removing the trailing characters.

example:
--------
string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))

Output:
-------
xoxo love xoxo
lov
  xoxo love xoxo
droid is awesome

-->Here, we can see that the first expression string.strip() without any arguments removed the whitespaces from the left and right of string.

string.strip(' xoe') - Removes all whitespace, x, o, and e that lead or trailed the string.
string.strip('stx') - Since string has whitespace at the beginning and end, this expression does not change the string. x is not removed since it is at the middle of the string (whitespaces lead and trail the string)
string.strip('an') - Removes an leading the string.

::-->The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).

Syntax : string.strip([chars])
chars (optional) - a string specifying the set of characters to be removed from the left and right part of the string.

-->The strip() method removes characters from both left and right based on the argument (a string specifying the set of characters to be removed).
Note: If the chars argument is not provided, all leading and trailing whitespaces are removed from the string. strip() returns a copy of the string with both leading and trailing characters stripped.

-->When the character of the string in the left mismatches with all the characters in the chars argument, it stops removing the leading characters.
Similarly, when the character of the string in the right mismatches with all the characters in the chars argument, it stops removing the trailing characters.

example:
--------
string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))

Output:
-------
xoxo love xoxo
lov
  xoxo love xoxo
droid is awesome

-->Here, we can see that the first expression string.strip() without any arguments removed the whitespaces from the left and right of string.

string.strip(' xoe') - Removes all whitespace, x, o, and e that lead or trailed the string.
string.strip('stx') - Since string has whitespace at the beginning and end, this expression does not change the string. x is not removed since it is at the middle of the string (whitespaces lead and trail the string)
string.strip('an') - Removes an leading the string.

"""