'''
Exercise 6: Tax and Tip
The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values are displayed using two decimal places.
'''

# solution 1:
# ---------
amount = float(input('enter the bill : '))
tax = amount * (10 / 100)
tip = amount * (18 / 100)
grand_total = amount + tax + tip
print("\n----------RECIEPT------------\n")
print('amount      : ', amount)
print('tax amount  : ', round(tax, 2))
print('tip amount  : ', round(tip, 2))
print('grand total : ', grand_total)


# solution 2:
# -----------
amount = float(input('enter the bill : '))
tax = amount * (10 / 100)
tip = amount * (18 / 100)
grand_total = amount + tax + tip
print("\n----------RECIEPT------------\n")
print("amount         : {:.2f}".format(amount))
print("tax amount     : {:.2f}".format(tax))
print("tip amount     : {:.2f}".format(tip))
print("grand total is : {:.2f}".format(grand_total))

