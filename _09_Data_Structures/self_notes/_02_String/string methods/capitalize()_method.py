"""

-->The capitalize() function doesn't take any parameters. This method returns a strign with the first letter capitalize and all other characters lowercased. It doesn't modify the original string.

example:
--------
string = 'hello world'
print(string.capitalize())
output:
-------
Hello world

-->if the string is empty, it prints nothing. what if the starting character is the number..?

string = '10hello world'
print(string.capitalize())

output:
-------
10hello world

-->Not only the number, if there is any operator or special character at the first position of the string, it prints the string as it is.


"""