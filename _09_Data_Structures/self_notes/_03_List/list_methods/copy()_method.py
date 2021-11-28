
"""

copy()
-------
list1 = [1, 2, 3, 4, 5]
print("Before copy list1    : ", list1)
list2 = list1.copy()  # individual copy
print("After copy list2     : ", list2)
print("Normal copy function : ", id(list1), id(list2))
list1.append(100)

print("After append : list1 :", list1)
print("After append : list2 :", list2)

# 2nd way of copy
------------------
list1 = [1, 2, 3, 4, 5]
list2 = list1
print("Variable  copy : ", id(list1), id(list2))
list1.append(100)
print("After var copy :", list1, list2)
list2.extend([11, 22])
print("After var copy :", list1, list2)


print("--------Shallow copy--------------")

# Shallow copy : copy()   -->   [1,2,3,4,5,6]
list1 = [1, 2, 3]
list2 = list1.copy()
print("Before : ", list1, list2, id(list1), id(list2))
list2.append(100)
print("After : ", list1, list2, id(list1), id(list2))


list1 = [1, 2, 3, [100, 200]]
list2 = list1.copy()
print("Before : ", list1, list2, id(list1), id(list2))
list2[3].append(300)
print("After : ", list1, list2, id(list1), id(list2))

print("--------Deep copy--------------")
from copy import deepcopy
list1 = [1, 2, 3]
list2 = deepcopy(list1)
print("Before : ", list1, list2, id(list1), id(list2))
list2.append(100)
print("After : ", list1, list2, id(list1), id(list2))


list1 = [1, 2, 3, [100, 200]]
list2 = deepcopy(list1)
print("Before : ", list1, list2, id(list1), id(list2))
list2[3].append(300)
print("After : ", list1, list2, id(list1), id(list2))

"""