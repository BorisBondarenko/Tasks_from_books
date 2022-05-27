question = 'Tell me any number and then I\'ll tell you is even this or odd number. '

answer = int(input(question))

if answer % 2 == 0:
    print(f'The number {answer} is even!')
else:
    print(f'The number {answer} is odd!')
