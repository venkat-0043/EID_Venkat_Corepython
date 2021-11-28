
"""
#REQ : print the numbers divisable by 5 from starting from 1 to 100

for  i in range(1,101):
    if i % 5 == 0:
        print(i, end = ' ')

output :
5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100

"""


"""
#REQ : remove all the elements in a list one item at a time.
#STATE : value = list()
#BEHAVIOUR : write a loop which removes items in a list one by one until the list is empty.

solution :
-----------
list1 = [1,2,3,4,5,6]

for i in range(len(list1)):
    list1.pop()

print(list1)

"""


"""
-->Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 

solution:
---------
result = []
for i in range(1500, 2701):
    if i % 5 == 0 and i % 7 == 0:
        result.append(i)

print('numbers divisible by 5 and 7 are : ', result)

"""


"""
-->Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

solution:
----------
#printing the first half of the pattern
for i in range(1,6):
    print(i * '* ')

#printing the second half of the pattern
for i in range(4, 0,  -1):
    print(i * '* ')

"""


"""
-->Write a Python program that accepts a word from the user and reverse it.

solution 1:
-----------
word = input('enter the word to reverse : ')
word1 = word[-1 : : -1]
print(word1)

solution 2:
-----------
word = input('enter the word to reverse')
word2 = []
for i in range(-1, -(len(word) + 1), -1):
    word2.append(word[i])
print(''.join(word2))

solution 3:
-----------
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

"""


"""
-->program to count the number of even and odd in a series

solution:
---------
even = 0
odd = 0
for i in range(1,11):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('number of even numbers ' , even)
print('number of odd numbers ' , odd)

"""


"""

-->write a program to print all the number accept 3 and 6

solution 1 using for loop:
------------------------
list1 = [3,6]
for i in range(0,10):
    if i not in list1:
        print(i)

solution 2 using for loop:
--------------------------
for i in range(0,10):
    if i == 3 or i == 6:
        continue
    print(i)
    
"""


"""
-->Write a Python program which takes two digits m(row) and n(column) as input and generates a two - dimensional
array. The element value in the i - th row and j - th column of the array should be i * j. Go to the editor
Note:
i = 0, 1.., m - 1
j = 0, 1, n - 1.

Test
Data: Rows = 3, Columns = 4
Expected
Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

solution:
---------
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))

# this returns the matrix full of zeros
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_list)

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row * col

print(multi_list)

"""


"""
-->Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.

solution:
---------
chars = input("enter the comma seperated binary values")

#split the string
chars_values = chars.split(',')
for i in chars_values:

    if int(i, 2) % 5 == 0:
        print(int(i, 2), i)

"""



"""
-->Write a Python program that accepts a string and calculate the number of digits and letters.

solution:
---------
value = input('enter the string')
digits = 0
chars = 0
for i in value:

    if i.isdigit():
        digits += 1

    elif i.isalpha():
        chars += 1

    else:
        pass

print('Digits : ', digits)
print('letters : ', chars)

"""


"""

-->Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

solution 1:
-----------
for i in range(100, 401):
    if i % 2 == 0:
        print(i, end = ', ')

solution 2: using the list comprehensions:
-----------
numbers = [i for i in range(100, 401) if i % 2 == 0]
for i in numbers:
    print(i, end = ', ')

solution 3:
-----------
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))

"""


"""
-->Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999

solution:
---------
for i in range(1, 10):
    print(i * str(i))

"""

"""
-->Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

solution:
---------
#this is for rows
for i in range(1, 6):
    #this is for columns
    for j in range(1, i+1):
        print(j, end = ' ')
    print()

"""


"""
-->Write a program to use for loop to print the following reverse number pattern
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

solution :
----------
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print()


"""