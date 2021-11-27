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










'''
'''
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
