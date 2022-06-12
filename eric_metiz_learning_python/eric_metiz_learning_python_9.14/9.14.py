from random import choice

lst = list(range(1, 11)) + ['A', 'B', 'W', 'X']

print('You have a winning-lottery number:')
for i in range(4):
    print(choice(lst), end='')
