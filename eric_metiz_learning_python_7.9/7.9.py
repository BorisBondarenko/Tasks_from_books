sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'vegetables', 'cheese', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('Pastrami not in the sandwich_orders.\n')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'I made your {order} sandwich.')
    finished_sandwiches.append(order)

print('\nAll this sandwiches is ready:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()} sandwich')
