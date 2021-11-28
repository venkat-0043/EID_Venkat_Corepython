"""
center():
--------


-->the center() method retuns a string which is padded with the specified character.
syntax : string.center(width[, fillchar])

-->the center() takes 2 arguments :
width : lenth of the string with padded character
fillchar(optional) : padding character. The fillchar argument is optional. if not provided space is take as default argument. for fillchar we can give any character like %, & (,), etc.

example:
--------
string = 'hello world'
result = string.center(25, '*')
print(result)

output:
-------
*******hello world*******

example:
---------
string = 'hello world'
#without the fillchar, by defualt it takes space
result = string.center(25)
print(result)

output:
-------
       hello world

"""