"""

-->the update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/values pairs. The update() method returns None and updates the original dictionary.

example:
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
dict2 = {'Language' : "English"}

print(dict1.update(dict2))
print(dict1)
output:
-------
None
{'eid': 123, 'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA', 'Language': 'English'}


example: pass the iterable to the update() method
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
dict2 = {'Language' : "English"}

print(dict1.update([['mobile', 987654321]]))
print(dict1)
output:
-------
None
{'eid': 123, 'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA', 'mobile': 987654321}


-->if we pass the same with different value to the update() method, then it updates the key with the new value.
example:
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
dict2 = {'Language' : "English"}

dict1.update([['eid', 456]])
print(dict1)
output:
-------
{'eid': 456, 'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA'}


example:
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}

dict1.update(a = 10, b= 30)
print(dict1)
output:
-------
{'eid': 123, 'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA', 'a': 10, 'b': 30}


example : update the dictionary, by taking the key, values at the run time
---------
n = int(input('enter the number of items : '))
dict1 = {}
for i in range(n):
    key = input('enter the key : ')
    value = input('enter the value for the key :')
    dict1.update({key : value})

print(dict1)
output:
-------
enter the number of items : 2
enter the key : 1
enter the value for the key :one
enter the key : 2
enter the value for the key :two
{'1': 'one', '2': 'two'}


example: this  is similar to above program. but used the dict() constructor
--------
n = int(input('enter the number of items : '))
dict1 = {}
for i in range(n):
    key = input('enter the key : ')
    value = input('enter the value for the key :')
    dict1.update(dict([(key, value)]))

print(dict1)
output:
-------
enter the number of items : 2
enter the key : 1
enter the value for the key :one
enter the key : 2
enter the value for the key :two
{'1': 'one', '2': 'two'}



"""