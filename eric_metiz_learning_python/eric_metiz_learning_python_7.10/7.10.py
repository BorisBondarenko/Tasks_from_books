# 25.05.2022

results = {}
reaction = True

while reaction != 'quit':

    next_action = input('Do you want to add next friend to vacation-list (yes/not): ')

    if next_action == 'yes':
        name = input('Enter name of your friend?: ')
        place = input('Where he(-she) planing to have vacation?: ')
        results[name.title()] = place.title()
    elif next_action == 'not':
        break
    else:
        print('Please enter correct answer (yes/not): ')
        continue

print('-' * 50)
for name, place in results.items():
    print(f'My friend {name.title()} wants to spend his holidays in {place.title()}.')
