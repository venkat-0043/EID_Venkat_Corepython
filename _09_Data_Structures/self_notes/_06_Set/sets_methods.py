"""

Sets are the unordered list of the value with no duplicates.
For example if we have 2 sets with common values. To find those common values we use the method intersection(). We can also perform the union operation using the method union().
Python’s set is an unordered collection in Python. It can be used to compute standard math operations, such as intersection, union, difference, and symmetric difference. Other collections — like list, tuple, and dictionary — don’t support set operations. Dict view objects are set-like, which allows set operations.

NOTE : SETS ONLY ACCEPT THE VALUE WHICH ARE IMMUTABLE, WHICH ARE NUMBERS, STRING, TUPLE. IF YOU ENTER THE GIVE LIST, SETS OR DICTIONARIES, IT RETURNS THE ERROR THAT THEY ARE NOT HASHABLE.

exmaple:
-------------
set1 = {'apple','mango','cherry','banana'}
set2 = {'apple','mango', 'papaya','gauva'}

new_set1 = set1.intersection(set2)
new_set2 = set1.difference(set2) #returns items in set1 not in set2
new_set3 = set.union(set2)
print('intersection : ',new_set1)
print('difference :', new_set2)
print('union :',new_set3)
output:
-------
intersection :  {'apple', 'mango'}
difference : {'cherry', 'banana'}
union : {'apple', 'gauva', 'mango', 'papaya'}

-->Normally to create the an empty list and tuple we can use the empty brackets or also use the methods list() and tuple(). For sets we can use the method set(). but can't creat empty set like set1 = {}. this creates an empty dictionary.
example:
------------
list1 = []
list1 = list()
print(list1)

tuple1 = ()
tuple1 = tuple()
print(tuple1)

set1 = {} #this creates a new dictionary
set1 = set()#this creates an empty set
print(set1)

-->the operations that we can perform on the sets are
union()
update()
intersection()
intersection_update()
difference()
difference_update()
symmetric_difference()
symmetric_difference_update()
isdisjoint()
issubset()
issuperset()
clear()

union():
--------
Return a new set with elements from the set and the other. It’s performed by union() or by using the | operator
Syntax : union(*others)

Difference between the union() method and the | operator:
union(): It’ll accept any iterables like list, tuples as an argument
| operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

update():
---------
It updates the set, adding elements from the other. But it won’t repeat elements. All elements in the set are unique. It’s performed by using update() or by using the |= operator. The return type is None. It’ll modify the original set itself.
Syntax : update(*others)
set |= other | ...

Difference between the update() method and the |= operator:
update(): It’ll accept any iterable as an argument
|= operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

intersection():
---------------
Return a new set with elements common to the set and the other. It’s performed by intersection() or by using the &operator.
Syntax : intersection(*others)
set & other & ...

Difference between the intersection() method and the & operator:
intersection(): It’ll accept any iterable as an argument
& operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

intersection_update():
----------------------
It updates the set, keeping only elements found in it and the other. It’s performed by using intersection_update() or by using the&= operator. The return type is None. It’ll modify the original set itself.
Syntax : intersection_update(*others)
set &= other & …

difference():
-------------
Returns a new set with elements in the set that aren’t in the other. It’s performed by difference() or by using the -operator.
Syntax
difference(*others)
set - other - ...

Difference between the difference() method and the -operator:
difference(): It’ll accept any iterable as an argument
- operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

difference_update():
--------------------
Removes the element from the set that’s also present in the other set. It’s performed by using the -= operator or by using the difference_update() method. The return type is None. It’ll modify the original set itself.
Syntax : difference_update(*others)
set -= other | ...

Difference between the difference_update() method and the
-= operator:
difference_update(): It’ll accept any iterable as an argument
-= operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

symmetric_difference():
-----------------------
Return a new set with elements in either the set or other but not both. It’s performed by symmetric_difference() or by using the ^ operator.
Syntax : symmetric_difference(other)
set ^ other

The symmetric_difference() method isn’t supported by multiple sets. If more than two sets are given, it’ll raise a TypeError. But we can find the symmetric_difference of multiple sets using ^

The difference between the symmetric_difference method and the& operator:
symmetric_difference(): It’ll accept any iterable as an argument. This method doesn’t allow for multiple sets.
^ operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError. By using the ^ operator, you can find the symmetric_difference between multiple sets.

symmetric_difference_update():
------------------------------
Updates the set, keeping only elements found in either set but not in both. It’s performed by using symmetric_difference_update() or by using the ^= operator. The return type is None. It’ll modify the original set itself.
Syntax : symmetric_difference_update(other)
set ^= other

isdisjoint():
-------------
Returns True if the set has no elements in common with the other. Sets are disjointed if and only if their intersection is the empty set.
Syntax : isdisjoint(other)

issubset():
Test whether every element in the set is in other.
Syntax: issubset(other)
set <= other
Proper subset:
--------------
Test whether the set is a proper subset of other — that is, set <= other and set != other.
Syntax
set < other

Example: Check whether set A is a proper subset of B
If both sets are equal, this means A.issubsetset(B) returns True. But the proper subset A<B will return False.
A={1,2,3,4,5}
B={4,5,6,7,8}
print (A<B)#Output: False

A={1,2,3,4,5}
B={1,2,3,4,5}
print (A<B)#Output: False

A={1,2,3}
B={1,2,3,4,5}
print (A<B)#Output: True

issuperset():
-------------
Test whether every element in other is in the set.
Syntax : issuperset(other)
set >= other
Proper superset:
----------------
Test whether the set is a proper superset of other— that is, set >= other and set != other.
Syntax
set > other
Example: Check whether set A is a proper superset of B.
If both sets are equal, it means A.issuperset(B) returns True. But the proper superset A>B will return False.
A={1,2,3,4,5}
B={4,5}
print (A>B)#Output: True

A={1,2,3,4,5}
B={1,2,3,4,5}
print (A>B)#Output: False

A={1,2,3}
B={1,2,3,4,5}
print (A>B)#Output: True


"""