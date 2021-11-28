
"""
example:
---------
#REQ : print the number in the descending order from 5 to 0
#STATE : n = 5
#BEHAVIOUR :
n = 5
while n > 0:
    n -= 1
    print(n)
"""

"""
-->Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

solution using while loop:
--------------------------
n = 0

#filtering condition, setting the upper limint to 50.
while n <= 50:
    if n % 3 == 0:
        print('fizz', end = '\n')
    elif n % 5 == 0:
        print('Buzz', end = '\n')
    elif n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz", end = '\n')
    else:
        print(n)
    n += 1

"""


"""
#REQ : prints the numbers in the descening order starting from 5, stop printing when number is 2
#STATE : num = 5
#BEHAVIOUR : start printing with upper value 5 and exit when value is 2.

n = 5
while n > 0:
    if n == 2:
        break
    print(n)
    n -= 1

"""


"""
#REQ : remove all the elements in a list one item at a time.
#STATE : value = list()
#BEHAVIOUR : write a loop which removes items in a list one by one until the list is empty.

solution 1:
---------
print("---------deleting the items in the list------------")

list_items = [1, 2, 3, 4]
while list_items:
    print(list_items.pop(), 'is deleted')

print("end of the loop")

"""


"""
#REQ : check if a value is in the list
#STATE : INPUT = ANY VALUE, list_items = list()
#BEHAVIOUR : write a loop to check if the input value is present in the list, if not print a friendly message and then exit

a = int(input('enter the number'))
list1 = [1,2,3,4,5,6]

#validating if the list is empty or not
while list1:
    if a in list1:
        print('value is in the sequence')
        break
    else:
        print('value is not in the sequence')
        break
else:
    print('may be the list is empty')

"""


"""
#REQ : validate the username and password
#STATE : Logins = dict{username : password}, input = username, password = password. both are of type string type
#BEHAVIOUR : first validate username, if true then only validate the relavent user's password, otherwise display the status message to the user

logins = {'user1' : 'password1', 'user2' : 'password2', 'user3' : 'password3'}
user_name = input('enter the username : ')

while user_name:
    if user_name in logins.keys():
        password = input('enter the password : ')
        if password == logins[user_name]:
            print('login successful : ')
            break
        else:
            print('password is wrong, login again : ')
            break
    else:
        print("user name is wrong")
        break

"""


"""
-->Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

solution:
---------
import random
target_num = random.randint(1,9)
guess_num = int(input('enter the number between 0 and 9 to guess : '))

while target_num != guess_num:
    guess_num = int(input('wrong, try again : '))
else:
    print('well guessed')

"""

"""
-->Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

solution:
---------
import random
target_num = random.randint(1,9)
guess_num = int(input('enter the number between 0 and 9 to guess : '))

while target_num != guess_num:
    guess_num = int(input('wrong, try again : '))
else:
    print('well guessed')
"""


"""
-->print all the numbers from 1 to 10 accept 3 and 6.
n = 0
while n < 10:
    n += 1
    if n == 3 or n == 6:
        continue
    print(n)

"""


"""

-->write a program to print the first 10 fibonacci numbers

solution :
----------
n = 0
a, b = 0, 1

#here is n used to print n number of fibonacci numbers
while n <= 10:
    print(a, end = ', ')    
    a, b = b, a + b
    n += 1

"""


"""

-->write a program to print the fibonacci numbers from 0 to 50

solution:
---------
#Write a Python program to get the Fibonacci series between 0 to 50.

n = 0
a, b = 0, 1

#below loop trying to print the first 20 fibonacci numbers
while n <= 20:

    #this is the filter condition
    if a < 50:
        print(a, end = ', ')    
    a, b = b, a + b
    n += 1


"""


"""

-->Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

Solution:
---------
list1 = []
while True :
    l = input('enter the string : ')
    if l:
        list1.append(l.lower())
    else:
        break

#this is to loop over the list of lines.
for line in list1:
    print(line)

"""


"""
-->Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number. For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10).

solution 1:
-----------
total = 0
n = 0
while n <= 10:
    total += n
    n += 1
print(total)

"""