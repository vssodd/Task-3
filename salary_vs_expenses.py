hours_worked = int(input('Enter hours worked: '))
credit_left = int(input('Enter remaining credit to pay: '))
food_expense = int(input('Enter food expenses: '))

expenses = credit_left + food_expense
salary = (200 * hours_worked) / (2 ** 3) + hours_worked  # Custom salary formula

if salary >= expenses:
    print('You’ve earned enough. Time to rest!')
else:
    print('Not enough earnings. You need to work more!')
