class User():
    def __init__(self, first_name: str, last_type: str, age: int):
        self.first_name = first_name.title()
        self.last_type = last_type.title()
        self.age = age

    def describe_user(self):
        print(f'User\'s full name is: {self.first_name} {self.last_type}')
        print(f'User\'s age is: {self.age}\n')

    def greet_user(self):
        print(f'Hello dear {self.first_name}! We so happy to see you here!\n')


user_1 = User('boris', 'bondarenko', 29)
user_2 = User('sofiia', 'chernenka', 27)
user_3 = User('mykola', 'chernenkyj', 27)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
