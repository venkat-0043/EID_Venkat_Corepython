"""
requirement :
-------------
-->take a list of values(may contain the duplicates). add each element of the list with other individual elements, if the sum if 7, then add the 2 values as a pair of tuple into a list like [(2,5), (1,6)]. if the result contain (2,5) then it should not contian (5,2).
"""

# solution :
# -----------
list1 = []
for i in range(int(input('how many values you want to enter : '))):
    n = int(input('enter the value : '))
    list1.append(n)

result = []

# adding each element in the list with other elements. here used set(list1) is reduce the number of iterations by
# avoiding the duplicates. if we want we can simply write without converting into the set.

for i in set(list1):
    for j in list1:
        if i + j == 10:
            # sorting to avoid the duplicates.
            tuple1 = tuple(sorted([i, j]))
            if tuple1 not in result:
                result.append(tuple1)

print(result)
