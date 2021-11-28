"""

-->The get() method returns the value for the specified key if the key is in the dictionary. if that value is not in the dictionary, by default it returns None. returns value if the key is not found and value is specified. The method is very useful to look up keys you don’t know are in the dictionary to avoid KeyErrors.

Syntax : dict.get(key[, value])

key - key to be searched in the dictionary
value (optional) - Value to be returned if the key is not found. The default value is None.


example: returns the value for the specified key if key is in the dictionary.
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
print(dict1.get('a'))
output:
-------
apple


example: returns None if the key is not found and value is not specified.
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
print(dict1.get('c'))
output:
-------
None


example: returns value if the key is not found and value is specified.
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
print(dict1.get('c', 'camel'))
output:
-------
camel

"""