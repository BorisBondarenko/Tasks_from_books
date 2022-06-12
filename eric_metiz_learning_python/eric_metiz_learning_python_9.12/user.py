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


