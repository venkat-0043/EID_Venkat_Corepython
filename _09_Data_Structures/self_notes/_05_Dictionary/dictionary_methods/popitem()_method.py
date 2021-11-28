"""

-->The popitem() method removes and returns the last element(key, value) pair inserted into the dictionary.

syntax : dict.popitem()

The popitem() method removes and returns the (key, value) pair from the dictionary in the Last In, First Out (LIFO) order. Returns the latest inserted element (key,value) pair from the dictionary.
Removes the returned element pair from the dictionary.

Note: Before Python 3.7, the popitem() method returned and removed an arbitrary element (key, value) pair from the dictionary.

example:
---------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
print('removing last key value : ', dict1.popitem())
print('new dictionary : ', dict1)
output:
-------
removing last key value :  ('Nationality', 'USA')
new dictionary :  {'eid': 123, 'ename': 'Guido', 'salary': 10000}

example:
--------
dict1 = {'eid' : 123, 'ename' : 'Guido', 'salary' : 10000, 'Nationality' : 'USA'}
dict1.update({'a' : 20})
dict1.update({'b' : 30})
print('removing last key value : ', dict1.popitem())
print('new dictionary : ', dict1)
output:
-------
removing last key value :  ('b', 30)
new dictionary :  {'eid': 123, 'ename': 'Guido', 'salary': 10000, 'Nationality': 'USA', 'a': 20}


example: CAN'T PERFORM THE POPITEM() ON THE EMPTY DICTIONARY.
--------
dict1 = {}
print('removing last key value : ', dict1.popitem())
print('new dictionary : ', dict1)
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    print('removing last key value : ', dict1.popitem())
KeyError: 'popitem(): dictionary is empty'


example:
--------
print('removing last key value : ', dict().popitem())
output:
-------
Traceback (most recent call last):
  File "C:\Users\this\Desktop\sample1.py", line 2, in <module>
    print('removing last key value : ', dict1.popitem())
KeyError: 'popitem(): dictionary is empty'


"""