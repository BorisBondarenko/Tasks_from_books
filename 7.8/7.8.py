sandwich_orders = ['tuna', 'vegetables', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'I made your {order} sandwich.')
    finished_sandwiches.append(order)


print('\nAll this sandwiches is ready:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()} sandwich')