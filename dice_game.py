guest_die = int(input('Guest’s die roll: '))
owner_die = int(input('Owner’s die roll: '))

total = guest_die + owner_die
print('Total score:', total)

if guest_die >= owner_die:
    print('The guest pays.')
else:
    print('The owner pays.')

print('\nGame over.')
