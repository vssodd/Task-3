a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a > b:
    max_value = a
else:
    max_value = b

if c > max_value:
    max_value = c

print('The maximum number is:', max_value)
