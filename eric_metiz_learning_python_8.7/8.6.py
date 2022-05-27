def make_album(author, album, songs_amount=None):
    if songs_amount:
        return {author: album, 'Amount of songs': songs_amount}
    else:
        return {author: album}


print(make_album('Guns N\' Roses', 'Appetite for Destruction'))
print(make_album('Thievery Corporation', 'Radio Retaliation'))
print(make_album('Linkin Park', 'Meteora'))
print(make_album('The War on Drugs', 'A Deeper Understanding', 10))
