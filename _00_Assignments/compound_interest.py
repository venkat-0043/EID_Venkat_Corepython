"""
Exercise 9: Compound Interest
------------------------------
-->Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.
"""
# solution 1:
# -----------
amount = float(input('enter the amount '))
interest = 0.04
total = 0

# this only calculates the first 3 years
for year in range(1, 4):
    if year == 1:
        total = amount + amount * interest
        print('after ', year, ' years', round(total, 2))

    if year == 2:
        total = total + (total * interest)
        print('after ', year, ' years', round(total, 2))

    if year == 3:
        total = total + (total * interest)
        print('after ', year, ' years', round(total, 2))

# solution 2 : the above code is only for 3 years. if you want for many number of years, use the below code.
# ------------
amount = float(input('enter the amount : '))
interest = 0.04
years = int(input('enter the number of years : '))

for year in range(1, years + 1):
    amount = amount + (amount * interest)
    print("after ", year, ' years : ', round(amount, 2))
