def make_shirt(size='l', text='I love Python'):
    answer = 'The order is ready.'
    answer += f'\nYour shirt has size {size.title()}, and cool text in the front: \"{text.title()}\"\n'
    print(answer)


make_shirt()
make_shirt('m', 'Who is John Gault?')
