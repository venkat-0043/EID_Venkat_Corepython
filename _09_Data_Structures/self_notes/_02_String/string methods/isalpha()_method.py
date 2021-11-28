
"""

isalpha():
----------

-->The isalpha() method returns True if all characters inthe string are alphabets. if not it returns False.

syntax : string.isalpha()

-->isalpha() don't take any parameters. The isalpha() return :
True : if all the characters in the string are alphabets(can both lowercase and uppercase)
False : if at least one character is not alphabet.

example:
--------
string = "hellopython"
print(string.isalpha())

output:
-------
True

example:
--------
string = "hello python"
print(string.isalpha())
output:
-------
False

-->This return false because it has the space in it.

example: check with numbers
--------
string = "python 3.8"
print(string.isalpha())
output:
-------
False

example: count number if alphabets in the string.
--------
string = 'hello world'
count = 0
#counting the character
for i in string:
    if i.isalpha():
        count += 1

print('total characters in string are : ', count)
output:
-------
total characters in string are :  10

"""