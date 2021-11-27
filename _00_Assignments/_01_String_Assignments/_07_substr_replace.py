# P07. REQ : Substring replacement

'''
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
'''
'''
1. CRUD       -->  Retrieval
2. STATE      -->  string 
3. BEHAVIOR   -->  int  |  =   +=    |   for   
'''

# 0. Mathematics 80%
'''

'''

# 1.Builtin functions 80%

print("-----1. Builtin Functions--------")

string = 'hello world'

new_string = string.replace('world', 'earth')
print(new_string)


# 2. Algorithm  80%

print("--------2. Algorithm----------")

string = 'hello world'

if 'world' in string:
    new_string = string.replace('world', 'earth')
else:
    print('substring not found')

print(new_string)



# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")


def str_replace():
    string = 'hello world how are you'

    string1 = string.split('world')
    print(string1)

    print('earth'.join(string1))


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
