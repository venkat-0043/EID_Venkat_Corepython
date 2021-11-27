'''
requirement:
-------------
-->takes 6 subject marks and calculate avg, if avg > 90 then check again if min 3 subjects marks is greater than 95 then print 'gold medal and distinction', if avg is between 75 and 90 print('distinction'), if avg < 75 print 'failed'.
'''
# solution:
# ---------
number = int(input('enter the number of subjects'))
marks_list = []
for i in range(1, number + 1):
    marks = int(input('enter the marks for subject : '))
    marks_list.append(marks)

avg = sum(marks_list) / number
print(avg)

count = 0
for i in range(number):
    if marks_list[i] >= 95:
        count = count + 1

if avg > 90.0:
    if count >= 3:
        print("gold medal and distinction")
    else:
        print('distinction')

elif 75.0 < avg < 90.0:
    print('average')


else:
    print('failed')
