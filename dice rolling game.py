import random

try:
    min_value = int(input('Enter the minimum value of the die: '))
    max_value = int(input('Enter the maximum value of the die: '))
except:
    print('Input invalid program will revert to defaults.')
    min_value = 1
    max_value = 6

again = True

while again:

    print(random.randint(min_value, max_value))

    another_roll = input('want to roll the die again? ')

    if another_roll.lower() == 'yes' or another_roll.lower() == 'y':
        continue
    else:
        break
