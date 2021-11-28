
"""

-->The rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed).

Example:
--------
title = 'Python Programming   '

# remove trailing whitespace print(title.rstrip())
# Output: Python Programming

Syntax : string.rstrip([chars])
chars (optional) - a string specifying the set of trailing characters to be removed.
The rstrip() removes characters from the right based on the argument (a string specifying the set of characters to be removed).

-->If chars argument is not provided, all whitespaces on the right are removed from the string. The rstrip() returns a copy of the string with trailing characters stripped.

-->All combinations of characters in chars argument are removed from the right of the string until the first mismatch.

Example: Working of rstrip()
random_string = 'this is good    '

# Trailing whitespace are removed
print(random_string.rstrip())

# 'si oo' are not trailing characters so nothing is removed
print(random_string.rstrip('si oo'))

# in 'sid oo', 'd oo' are the trailing characters, 'ood' is removed from the string
print(random_string.rstrip('sid oo')) website = 'www.programiz.com/'

print(website.rstrip('m/.'))

Output:
-------
this is good
this is good
this is g
www.programiz.co


"""