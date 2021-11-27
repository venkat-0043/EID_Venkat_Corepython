"""
requirement:
------------
We have to take input of subjects and marks from user
If No.of subjects is between 3 - 7
    We have to find percentage of all subjects
    If total percentage is greater than 90 --> awarded distinction
    If total percentage is between 75 to 90 --> awarded average
    If total percentage is less than 75:
        chance is given only if he score less than 75% in 3 subjects
        if he score less than 75% in more than 3 subjects he is given fail


If No.of subjects is greater than 7
    we have to find percentage of all subjects
    If total percentage is greater than 90 --> awarded distinction
    If total percentage is between 75 to 90 --> awarded average
    If total percentage is less than 75:
        chance is given only if the fail subjects average should be between 65 - 75
        else he will be given fail
        if he fail in more than 5 subjects he should be debarred
"""


# solution :
# ----------
def sub_between_3_to_7(n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input(f'enter the name of the subject {i} : ')
        # this checks if the marks are between 0 and 100
        while True:
            marks = int(input(f'enter the marks for the subject {subject} : '))
            if marks < 0 or marks > 100:
                print('enter the marks between 0 and 100... : ')
                continue
            marks_dict.update({subject: marks})
            marks_list.append(marks)
            break

    avg = (sum(marks_list)) / n

    # count number of subject whose marks are <= 75
    count = 0
    for i in marks_list:
        if i <= 75.0:
            count = count + 1

    print('\nResult : ', end=' ')
    if avg >= 90.0:
        print('Distinction')

    elif 75.0 <= avg <= 90.0:
        print('Average')

    elif avg < 75.0:
        if count <= 3 < number:
            print('passed')
        else:
            print('failed')

    print("\nyour marks list \n-----------------")
    for subject, marks in marks_dict.items():
        print(subject, ' : ', marks)
    print('\npercentage : {:.2f}%'.format(avg))


def sub_more_than_7(n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input(f"enter the name of the subject {i} : ")
        # this checks if the marks are between 0 and 100
        while True:
            marks = int(input(f'enter the marks for the subject {subject} : '))
            if marks < 0 or marks > 100:
                print('\nenter the marks between 0 and 100... : \n')
                continue
            marks_dict.update({subject: marks})
            marks_list.append(marks)
            break

    avg = (sum(marks_list) / n)

    # count number of subjects whose marks are between 65 and 75
    count = 0
    for i in marks_list:
        if i >= 65.0 and i <= 75.0:
            count = count + 1

    print('\nResult : ', end='')
    if avg >= 90.0:
        print('Distinction')

    elif 75.0 <= avg <= 90.0:
        print('Average')

    elif avg <= 75.0:
        if count == 3:
            print('Passed')

        elif count == 4:
            print('Failed')

        elif count >= 5:
            print('Debarred')

    print('\nyour marks list \n-----------------')
    for subject, marks in marks_dict.items():
        print(subject, ' : ', marks)
    print('\npercentage : {:.2f}'.format(avg))


number = 0

while True:
    number = int(input('enter the number of subjects : '))
    if 3 <= number <= 7:
        sub_between_3_to_7(number)

    elif number > 7:
        sub_more_than_7(number)

    elif number < 3:
        print('\nminimum 3 subject, enter again...\n')
        continue
    break
