def order_maker(*args):
    print('Your sandwich contain:')
    for i in args:
        print(f'  -{i}')

    print('It will be ready for you in couple minutes!')


components = ['tomato', 'chees', 'tuna']
order_maker(*components)
