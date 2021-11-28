
"""
count():
--------
-->The count() method returns the number of times the specified element appears in the tuple.

syntax : tuple.count(element)
element - the element to be counted

example:
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
print(tuple1.count(1))
output:
-------
3

example:
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
print(tuple1.count({'a' : 'apple'}))
output:
-------
1


example: print the elements which are repeated minimum 2 times.
--------
tuple1 = (1, 2, 3, 1, 2, 1, [1], 'python', {'a' : 'apple'})
repeated_elements = set()
for i in tuple1:
    if tuple1.count(i) >= 2:
        repeated_elements.add(i)

print('repeated elements are : ", repeated_elements)
output:
-------
repeated elements are :  {1, 2}

"""