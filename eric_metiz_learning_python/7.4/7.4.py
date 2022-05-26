reaction = True
question = 'What your next topping do you prefer for pizza? '

while reaction != 'quit':
    reaction = input(question)
    if reaction != 'quit':
        print(f'{reaction.title()} was added to order!')
    else:
        break