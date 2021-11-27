# P06. REQ : Append chars to string at end

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

string = 'hello worl'
list_string = [i for i in string]
list_string.append('d')

print(''.join(list_string))


# 2. Algorithm  80%

print("--------2. Algorithm----------")

string = 'hello worl'
string = string + 'd'
print(string)



# 3 Using Functions  ==> 50 programs
print("--------3 Using Functions----------")

def append_str():

    string = 'hello worl'
    string += 'd'
    print('string after append : ', string)


append_str()


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
