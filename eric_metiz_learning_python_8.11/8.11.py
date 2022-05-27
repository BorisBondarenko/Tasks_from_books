sent_messages = []


def show_messages(list):
    while list:
        message = list.pop()
        print(message)
        sent_messages.append(message)


to_send = ['Hello!', 'Добрый день!', 'Buenas tardes!']
show_messages(to_send[:])

print(to_send)
print(sent_messages)