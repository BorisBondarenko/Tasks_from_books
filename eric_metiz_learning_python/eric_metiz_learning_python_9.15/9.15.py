from random import choice

my_ticket = 'AW19'
lst = list(range(1, 11)) + ['A', 'B', 'W', 'X']

next_number = ''
counter = 0
while next_number != my_ticket:
    next_number = ''.join([str(choice(lst)) for i in range(4)])
    counter += 1

print(f'You are really lucky guy.\nWinning from {counter}th try.\nIt\'s so exited!')