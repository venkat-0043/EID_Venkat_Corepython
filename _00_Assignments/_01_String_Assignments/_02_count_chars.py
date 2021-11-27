# P2 : count the characters in a string

'''
Topics:
--------
Operators
DM vs Loops
Data structure
'''

'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''


# 0. Mathematics
# Implement the solutions in white paper
# take a input string
# take a count variable
# check the character using built-in method
# increment the count
# return the count

# 1.Builtin functions

print("-----1. Built Functions--------")

string = input('enter the string')
count = 0
for i in string:
    if i.isalpha():
        count += 1

print('number of characters are : ', count)

# 2. Algorithm

print("--------2. Algorithm----------")

# solution 1
string = input('enter the string')

count = 0
for i in string:
    if type(i) == str and ord(i) not in range(48, 58):
        count += 1

print('number of characters are : ', count)




# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def count_chars(string):

    count = 0
    for i in string:
        if i.isalpha():
            print(type(i))
            count += 1
    return count


string = input("enter the string")
print(count_chars(string))


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
