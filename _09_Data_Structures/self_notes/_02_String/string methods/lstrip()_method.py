
"""

lstrip():
----------

-->The lstrip() method returns a copy of the string with leading characters removed (based on the string argument passed).

-->The lstrip() removes characters from the left based on the argument (a string specifying the set of characters to be removed).

syntax : string.lstrip([chars])
chars (optional) - a string specifying the set of characters to be removed.
If chars argument is not provided, all leading whitespaces are removed from the string.

-->lstrip() returns a copy of the string with leading characters stripped.

-->All combinations of characters in the chars argument are removed from the left of the string until the first mismatch.

Example: Working of lstrip()
random_string = '   this is good '

# Leading whitepsace are removed
print(random_string.lstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))

print(random_string.lstrip('s ti'))

website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))
Output:
-------
this is good
   this is good
his is good
www.programiz.com/


"""
