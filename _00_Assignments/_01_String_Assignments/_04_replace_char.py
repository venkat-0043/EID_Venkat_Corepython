# P04: REQ : Replace the character in a string

'''
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
'''
'''
1. CRUD       -->  update
2. STATE      -->  string 
3. BEHAVIOR   -->     
'''

# 0. Mathematics 80%
'''

'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

string = 'hello world'

string1 = string.replace('l', 'L')
print('string before replace : ', string)
print('string after replace  : ', string1)


# 2. Algorithm  80%

print("--------2. Algorithm----------")

string = 'hello world'

list_string = list(string)
print(list_string)

for i in list_string:
    if i == 'l':
        list_string[list_string.index(i)] = 'L'

print(''.join(list_string))



# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")


def str_replace():

    string = 'hello world'

    list_string = []

    for i in string:
        if i == 'l':
            list_string.append('L')
        else:
            list_string.append(i)

    print('string after replace : ', ''.join(list_string))


str_replace()



# 4 OOPS              ==> 30 programs
print("--------4 Object Oriented----------")

# 5 Exception handling  ==> 15 programs
print("--------5 Exception handling----------")

# 6 File Handling  ==> 10 programs
print("--------6 File Handling----------")

# 7 Database interaction MVC  ==> 5 programs
print("--------7 Database interaction----------")



# 8 UI Interaction   ==> 3 programs
print("--------8 UI Interaction----------")
