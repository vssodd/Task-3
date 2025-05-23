item_1 = int(input('Enter the price of the first item: '))
item_2 = int(input('Enter the price of the second item: '))
item_3 = int(input('Enter the price of the third item: '))

total = item_1 + item_2 + item_3

if total > 10000:
    discount = total * 0.10
    total -= discount
    print('A 10% discount has been applied.')
else:
    print('No discount applied.')

print('Total cost:', total)
