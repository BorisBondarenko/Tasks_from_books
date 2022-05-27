def make_album(author, album, songs_amount=None):
    if songs_amount:
        return {author: album, 'Amount of songs': songs_amount}
    else:
        return {author: album}


while True:
    print('\n(Enter "q" at any time to quit)')

    inp_author = input('Enter Author or Group: ')
    if inp_author == 'q':
        break

    inp_album = input('Enter Album name: ')
    if inp_album == 'q':
        break

    inp_am_of_songs = input("Tell how many songs in album? (not necessary): ")
    if inp_am_of_songs == 'q':
        break

    print(make_album(inp_author, inp_album, inp_am_of_songs))