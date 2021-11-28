
"""

append():
---------
-->With .append(), you can add items to the end of an existing list object. You can also use .append() in a for loop to populate lists programmatically. Python’s .append() takes an object as an argument and adds it to the end of an existing list, right after its last element:

example:
--------
numbers = [1,2,3,4]
numbers.append(5)
print(numbers)
output:
-------
[1, 2, 3, 4, 5]


example: adding a new list using append()
--------
numbers = [1,2,3,4]
numbers2 = [6,7,8,9]
numbers.append(numbers2)
print(numbers)
output:
-------
[1, 2, 3, 4, [6, 7, 8, 9]]

-->with append() method, it you add the single element, it will added as individual element, if you add another list, that list is added with same structure, which means it will be added as the sublist. this works same for tuple, set, dict.

example:
--------
numbers = [1,2,3,4]
numbers2 = (6,7,8,9)
numbers.append(numbers2)
print(numbers)
output:
-------
[1, 2, 3, 4, (6, 7, 8, 9)]


-->usually the append() operation returns None. the reason list is mutable. so the lists are modified internally and it didn't  return any copy like strings.
example:
--------
numbers = [1,2,3,4]
numbers2 = (6,7,8,9)
return_value = numbers.append(numbers2)
print('the append returns : ',return_value)
output:
-------
the append returns :  None


append() use case:
------------------
-->One common use case of .append() is to completely populate an empty list using a for loop. Inside the loop, you can manipulate the data and use .append() to add successive results to the list.
example:
--------
numbers = [1,2,3,4]
numbers2 = []
for i in numbers:
    numbers2.append(i ** 2)

print(numbers2)
output:
-------
[1, 4, 9, 16]


example:
--------
my_list = [1,2,3,4,5,6,7,8,9]
num = []

for letter in 'abcd':
    for number in my_list:
        num.append((letter, number))
print(num)

output:
-------
[('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8), ('a', 9), ('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('b', 6), ('b', 7), ('b', 8), ('b', 9), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('c', 6), ('c', 7), ('c', 8), ('c', 9), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('d', 8), ('d', 9)]


-->append() is used to implement the stack and queues. this is advance topic.

"""