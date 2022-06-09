class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age

    def describe_user(self):
        print(f'User\'s full name is: {self.first_name} {self.last_name}')
        print(f'User\'s age is: {self.age}\n')

    def greet_user(self):
        print(f'Hello dear {self.first_name}! We so happy to see you here!\n')


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


admin = Admin('boris', 'bondarenko', 29)
admin.privileges.show_privileges()
