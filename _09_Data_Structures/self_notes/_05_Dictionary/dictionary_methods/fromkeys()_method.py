"""
-->the fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.

syntax : dictionary.fromkeys(sequence[, value])

sequence - sequence of elements which is to be used as keys for the new dictionary
value (Optional) - value which is set to each element of the dictionary

-->fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.
If the value argument is set, each element of the newly created dictionary is set to the provided value.

example: default value for keys is None
--------
keys = {'a', 'b', 'c', 'd'}
dict2 = dict.fromkeys(keys)
print(dict2)
output:
-------
{'c': None, 'a': None, 'd': None, 'b': None}

DOUBT
example : instead of dict.fromkeys(), we can use another dictionary, there is no change.
---------
keys = {'a', 'b', 'c', 'd'}
dict1 = {}
dict2 = dict1.fromkeys(keys)
print(dict2)
output:
-------
{'c': None, 'a': None, 'd': None, 'b': None}


example: we can use the keys of another dictionary also
--------
keys = {'a', 'b', 'c', 'd'}
dict1 = {'e': 5 , 'f' : 6 , 'g' : 7, 'h' : 8, 'i' : 9}
dict2 = dict.fromkeys(dict1.keys())
print(dict2)
output:
-------
{'e': None, 'f': None, 'g': None, 'h': None, 'i': None}


"""