question = 'For how many persons I must give you the table?: '

answer = int(input(question))

if answer >= 8:
    print('I think you must wait for it probaly 15-25 min.')
else:
    print('There is your table!')