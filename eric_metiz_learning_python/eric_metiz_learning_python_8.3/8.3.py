def make_shirt(size: str, text: str):
    answer = 'The order is ready.'
    answer += f'\nYour shirt has size {size.title()}, and cool text in the front: {text.title()}'
    print(answer)


make_shirt('m', 'Who is John Gault?')
