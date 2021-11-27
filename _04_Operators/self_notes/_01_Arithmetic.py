''''--------------Addition--------------'''
'''----------Case1----------------'''
a = 10
b = 20
c = a + b
print(a + b)
print(10 + 20)
print('The addition is : ', 30)

'''----------Addition with integer and float---------------'''

a = 10
b = 20.0
print('a + b is ', a + b) #returns the float value

a = 10
b = -20
print(a + (-b))  #returns 30.

'''------------Adding integers and boolean values---------------'''
a = 10
b = True
print('Adding 10 and True : ', a + b) #return 11, because True evaluates to True

a = 10
b = False
print('Adding 10 and False : ', a + b) #return 10, because False evaluates to  0

'''----------------Subtraction-------------------'''
a = 10
b = False
c = True
print(a - b) #return 10
print(a - c) #return 9

'''--------------Multiplication-----------------------'''
a = 10
b = 20
print('multiplication of a and ', a * b)


a = 10
b = False
print('multiplying 10 and False : ', a * False) #returns 0

a = 10
b = True
print('multiplying 10 and True : ', a * b) #return 10

a = 5
b = 'string'
print('multiplying 5 and string : ', a * b) #returns stringstringstringstringstring

a = 3
b = [1,2,3]
print('multiplying 5 and list : ', a * b)  #returns [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(a * [[1,2,3]]) #returns [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

a = 3
b = (1,2,3)
print('multiplying 3 and tuple : ', a * b) #returns (1, 2, 3, 1, 2, 3, 1, 2, 3)

a = 3
b = ((1,2,3))
print('multiplying 3 and tuple : ', a * b) #returns (1, 2, 3, 1, 2, 3, 1, 2, 3)
''' these kind of multiplication operations don't work on the dict and sets'''


'''---------------------Division------------------'''
a = 10
b = 20
print('division of 10 and 20 is : ', a / b) # returns 0.5
#by default the division returns the float.

a = 20.0
b = 10
print('the floor division of a and b is : ', a // b) #return 2.0
#in floor division if any value is float, the result will be float.































'''--------------Addition on data structures----------------'''
a = (1,2,3)
b = (4,5,6)
print('adding of tuples is ', a + b)

#Adding 2 lists
a = [1,2,3]
b = [4,5,6]
print('adding 2 lists is ', a + b)

#Adding 2 sets
a = {1,2,3}
b = {4,5,6}
c = a + b #TypeError: unsupported operand type(s) for +: 'set' and 'set'

#Adding 2  dictionaries
a = {'a' : 'apple'}
b = {'b' : 'ball'}
c = a + b #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'







