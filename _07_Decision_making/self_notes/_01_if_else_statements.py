'''
marks = int(input('enter the marks : '))

if marks >= 90 and marks <= 100:
    print('A grade')

elif marks>=75 and mark s < 90:
    print('B grade')

elif marks >=60 and marks < 75:
    print("C grade")

elif marks >=35 and marks < 60:
    print("D grade")

else:
    print("failed")

x = 0
y = 5

if x < y:     #thuth
    print('yes')

if  y < x:  #False
    print('yes')

if x:
    print('yes') #false

if y :  #True
    print('yes')

if x or y:    #Truth
    print("yes'")

if x and y:  #False
    print('yes')

if   'aul' in 'fault':  #Truth
    print("yes")

if 'quux' in ['foo', 'bar', 'baz']:  #false
    print("yes")

>>> raining = False
>>> print("Let's go to the", 'beach' if not raining else 'library')
Let's go to the beach
>>> raining = True
>>> print("Let's go to the", 'beach' if not raining else 'library')
Let's go to the library

>>> age = 12
>>> s = 'minor' if age < 21 else 'adult'
>>> s
'minor'

>>> 'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
'no'

a = 10
b = 20
m = a if a > b else b

>>> x = y = 40

>>> z = 1 + x if x > y else y + 2
>>> z
42

>>> z = (1 + x) if x > y else (y + 2)
>>> z
42

>>> s = ('foo' if (x == 1) else
...      'bar' if (x == 2) else
...      'baz' if (x == 3) else
...      'qux' if (x == 4) else
...      'quux'
... )
>>> s
'baz'



marks = int(input('enter the marks : '))

if marks >= 91 and marks <= 100:
    print('A grade')

elif marks>=76 and mark s <= 90:
    print('B grade')

elif marks > 61 and marks <= 75:
    print("C grade")

elif marks >=35 and marks <= 60:
    print("D grade")

else:
    print("failed")
'''

'''
solution 2:
-----------

if marks in range(90,101):
    print("A grade")

elif marks in range(75, 91):
    print('B grade')

elif marks in range(60, 75):
    print("C grade")

elif marks in range(35, 60):
    print("D grade")

else:
    print('failed')
'''

"""
-->take 4 subjects marks in the run time, calculate the average. display "passed with percentage" if each subject marks >= 35, else print "failed".

s1 = int(input('enter the marks'))
s2 = int(input('enter the marks'))
s3 = int(input('enter the marks'))
s4 = int(input('enter the marks'))
average = (s1 + s2 + s3 + s4)/4

if s1 < 35 or s2 < 35 or s3 < 35 or s4 < 35:
    print('failed')
else:
    print('passed with percentage', average, '%')
"""

"""
-->validate the subject marks, whether passed on not.

marks = int(input('enter the marks'))
if marks and 35 <= marks <= 100:
    print('passed')
else:
    print('failed')

"""

"""
check if a function is returnig a value or not:
-----------------------------------------------
def func():
    print("the main function is running")
    #return 10

if func():
    print("the main is returning some value")

else:
    print("the main function is not returning a value")

"""

"""
-->check the if id is matched with keys in the dictionary, else print id is not matched.

dict1 = {101 : 'emp1', 102 : 'emp2', 103 : 'emp3'}
id = int(input('enter the id'))
if id in dict1:
    print(dict1[id])
else:
    print('id is not matched')

"""

"""
leap year:
----------
-->any year divisable by 4 is leap year. if the year is divisable by 4 and is a century year, check if that year is divisable by 400. then only that year is the leap year. 

solution 1:
-----------
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')



year = int(input('enter the year'))
if year % 4 == 0 and year % 100 != 0  or year % 400 == 0:
    print('leap year')
else:
    print('not a leap year')

"""


"""
-->Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

solution using for loop:
------------------------
for i in range(1, 51):
    if i % 3 == 0:
        print('Fizz', end = '\n')
    elif i % 5 == 0:
        print("Buzz", end = '\n')
    elif i % 3 and i % 5 == 0:
        print("FizzBuzz", end = '\n')
    else:
        print(i)

"""

"""
-->Write
a
Python
program
to
check
a
triangle is equilateral, isosceles or scalene.

solution:
---------
a = int(input('enter the first side'))
b = int(input('enter the second side'))
c = int(input('enter the third side'))

if a == b == c:
    print('equilateral triangle')
elif a == b or a == c:
    print('isosceles triangle')
else:
    print('scalene triangle')

solution
2:
-----------
sides = {'a': None, 'b': None, 'c': None}

# taking the input for a,b,c at the run time.
for i in sides:
    sides[i] = int(input('enter the value'))
print(sides)

if sides['a'] == sides['b'] == sides['c']:
    print('equilateral triangle')

elif sides['a'] == sides['b'] or sides['a'] == sides['b']:
    print('isosceles triangle')
else:
    print('scalene triangle')

"""

"""
-->Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

solution using for loop:
------------------------
for i in range(1, 51):
    if i % 3 == 0:
        print('Fizz', end = '\n')
    elif i % 5 == 0:
        print("Buzz", end = '\n')
    elif i % 3 and i % 5 == 0:
        print("FizzBuzz", end = '\n')
    else:
        print(i)

"""


"""


-->Write a Python program to check the validity of password input by users. 
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

solution:#we also do this using the regular expressions.
---------
password = input("enter the password")
digits = 0
chars = 0
special = 0

#first calculate the number of digits, chars and special chars
for i in password:
        
    if i.isdigit():
        digits += 1

    elif i.isalpha():
        chars += 1

    elif i in ['$', '#', '@']:
        special += 1

    else:
        pass

#write the filter condition and then validate                   
if  6 <= len(password) <= 16:

    if digits and chars and special:
        print('password is valid')

    else:
        print('password is not valid')

else:
    print('password is very short')


"""


"""
-->Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given: [12, 75, 150, 180, 145, 525, 50]
output:
75
150
145

solution:
---------
numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break

    elif item > 150:
        continue

    elif item % 5 == 0:
        print(item)

"""
