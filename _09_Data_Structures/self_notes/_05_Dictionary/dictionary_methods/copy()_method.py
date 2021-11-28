"""

-->the copy() method returns the copy(shallow copy) of the dictionary. It doesn't modify the original dictionary.

Syntax : dict.copy()

example:
--------
dict1 = {'a' : 'apple' , 'b' : 'banana'}
new_dict1 = dict1.copy()
print('old dictionary : ', dict1)
print('copy of dictionary : ', new_dict1)
output:
-------
old dictionary :  {'a': 'apple', 'b': 'banana'}
copy of dictionary :  {'a': 'apple', 'b': 'banana'}

-->to check if it is copy or not, use membership operator 'is'.
example:
--------
dict1 = {'a' : 'apple' , 'b' : 'banana'}
new_dict1 = dict1.copy()
#print('old dictionary : ', dict1)
#print('copy of dictionary : ', new_dict1)
print(dict1 is new_dict1)
output:
-------
False


-->When the copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary. When the = operator is used, a new reference to the original dictionary is created.
example:
--------
dict1 = {'a' : 'apple' , 'b' : 'banana'}
new_dict1 = dict1
print(dict1 is new_dict1)
output:
-------
True


-->eventhought we clear the items in the copied dictionary, the original stays unchanged.
example:
--------
dict1 = {'a' : 'apple' , 'b' : 'banana'}
new_dict1 = dict1.copy()
#clearing the dictionary copy
new_dict1.clear()
print('original dictionary : ', dict1)
output:
-------
original dictionary :  {'a': 'apple', 'b': 'banana'}

"""