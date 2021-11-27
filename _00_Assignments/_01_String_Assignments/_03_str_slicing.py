# P03. REQ : String slicing

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
3. BEHAVIOR   -->  slice(), [:]   
'''

# 0. Mathematics

# Implement the solutions in white paper

# 1.Builtin functions

print("-----1. Built Functions--------")

string = input('enter the string')

# this slice object grabs the first 6 characters of a string
sliced_string = slice(6)
print(string[sliced_string])



# 2. Algorithm

print("--------2. Algorithm----------")

string = input('enter the string')

# first 5 characters
print(string[0 : 6])

# using negative index
print(string[::-1])



# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def str_slice():

    string = input('enter the string')
    sliced_string = slice(5)
    print(string[sliced_string])

str_slice()




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
