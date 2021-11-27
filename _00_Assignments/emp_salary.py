# solution 1:
# ---------
def salary(month):
    # calculates the net and total salary, call the expenditure()
    basic = float(input(f'enter the basic pay for month {month} : '))
    hra = float(input(f'enter the hra month {month} : '))
    special_allowance = float(input(f'enter the special allowance for month {month}: '))
    tax = float(input(f'enter the tax amount for month {month}: '))
    tot_sal = basic + hra + special_allowance + tax
    net_sal = basic + hra + special_allowance - tax
    print(f'\nnet salary for month {month} is {net_sal}\n')
    return expenditure(month, net_sal)


def expenditure(month, net_sal):
    # calculate the total expenditure and calls the tot_savings()
    food = float(input(f'enter the food expenses for month {month} : '))
    rent = float(input(f'enter the rent for the month {month} : '))
    total_exp = food + rent
    print(f'\nexpenses for the month {month} is {total_exp}')
    return tot_savings(month, net_sal, total_exp)


def tot_savings(month, net_sal, tot_exp):
    # calculate the savings
    savings = net_sal - tot_exp
    print(f'\nsavings for the month {month} is {savings}\n')
    return savings


# program starts from here.
emp_name = input('enter the name : ')
emp_id = input('enter the employee id : ')
months = int(input('enter the number of months : '))
savings = 0

for month in range(1, months + 1):
    savings = savings + salary(month)
if savings > 0:
    print(f'total savings for {months} months is {savings}')
    print('\n----------WINNER------------')
else:
    print(f'total savings for {months} months is {savings}')
    print('\n----------LOSER--------------')

'''
Note : here the salary(month) in the for loop contains the return value of total_savings(month, net_sal, tot_exp), because see below :
salary(month) calls salary(month) which is the first function
salary(month) calls the expenditre(month, net_sal)
expenditure(month, net_sal) call the total_savings(month, net_sal, tot_exp)
'''


# solution 2: ask the user if he has expenses this month, if yes take that expense and amount, if no exit the loop.
# ------------
def salary(month):
    # calculates the net and total salary, call the expenditure()
    basic = float(input(f'enter the basic pay for month {month} : '))
    hra = float(input(f'enter the hra month {month} : '))
    special_allowance = float(input(f'enter the special allowance for month {month}: '))
    tax = float(input(f'enter the tax amount for month {month}: '))
    tot_sal = basic + hra + special_allowance + tax
    net_sal = basic + hra + special_allowance - tax
    print(f'\nnet salary for month {month} is {net_sal}\n')
    return expenditure(month, net_sal)


def expenditure(month, net_sal):
    # calculate the total expenditure and calls the tot_savings()
    total_exp = 0
    while True:
        exp = input(f"do you have expediture for month {month}, enter yes or no : ")
        while exp == 'yes':
            exp_name = input(f'enter the name of expenditure for month {month} : ')
            exp_amount = float(input(f'enter the {exp_name} amount for the month {month} : '))
            total_exp += exp_amount
            decision = input(f'want to continue with another expenses for the month {month}, enter yes or no : ')
            if decision == 'yes':
                continue
            else:
                break
        break

    print(f'\nexpenses for the month {month} is {total_exp}')
    return tot_savings(month, net_sal, total_exp)


def tot_savings(month, net_sal, tot_exp):
    # calculate the savings
    savings = net_sal - tot_exp
    print(f'\nsavings for the month {month} is {savings}\n')
    return savings


# program starts from here.
emp_name = input('enter the name : ')
emp_id = input('enter the employee id : ')
months = int(input('enter the number of months : '))
savings = 0

for month in range(1, months + 1):
    savings = savings + salary(month)
if savings > 0:
    print(f'total savings for {months} months is {savings}')
    print('\n----------WINNER------------')
else:
    print(f'total savings for {months} months is {savings}')
    print('\n----------LOSER--------------')

'''
Note : here the salary(month) contains the return value of total_savings(month, net_sal, tot_exp), because see below :
salary(month) calls salary(month) which is the first function
salary(month) calls the expenditre(month, net_sal)
expenditure(month, net_sal) call the total_savings(month, net_sal, tot_exp)
'''
