"""

-->The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.

syntax : dict.setdefault(key[, default_value])

key - the key to be searched in the dictionary
default_value (optional) - key with a value default_value is inserted to the dictionary if the key is not in the dictionary. If not provided, the default_value will be None.

-->this method retuns value of the key if it is in the dictionary. None if the key is not in the dictionary and default_value is not specified. default_value if key is not in the dictionary and default_value is specified

example: retunns value of the key if it is in the dictionary
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
print(dict1.setdefault('a'))
print(dict1)
output:
-------
apple
{'a': 'apple', 'b': 'box'}


example: None if the key is not in the dictionary and default_value is not specified.
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
print(dict1.setdefault('c'))
print(dict1)
output:
-------
None
{'a': 'apple', 'b': 'box', 'c': None}


example: returns default_value if key is not in the dictionary and default_value is specified.
--------
dict1 = {'a' : 'apple' , 'b' : 'box'}
print(dict1.setdefault('c', 'carrot'))
print(dict1)
output:
-------
carrot
{'a': 'apple', 'b': 'box', 'c': 'carrot'}


"""