question = 'How old are you?: '
reaction = True

while reaction:
    reaction = input()

    if reaction.isdigit():
        reaction = int(reaction)
        if reaction < 3:
            print('For your child ticked is free!')
        elif 3 <= reaction <= 12:
            print('Your ticket price is 10$')
        elif 12 < reaction:
            print('Your ticket price is 15$')
    elif reaction == 'quit':
        break

print('Hope for your visit in our cinema!')
