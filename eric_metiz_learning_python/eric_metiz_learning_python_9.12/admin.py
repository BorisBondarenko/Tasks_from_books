from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban post', 'can ban user']

    def show_privileges(self):
        print('My privileges:')
        for i in self.privileges:
            print(f'- {i}')


class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()