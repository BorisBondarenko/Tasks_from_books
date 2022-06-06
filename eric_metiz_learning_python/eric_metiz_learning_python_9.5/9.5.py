class User():
    def __init__(self, first_name: str, last_type: str, age: int):
        self.first_name = first_name.title()
        self.last_type = last_type.title()
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'User\'s full name is: {self.first_name} {self.last_type}')
        print(f'User\'s age is: {self.age}\n')

    def greet_user(self):
        print(f'Hello dear {self.first_name}! We so happy to see you here!\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('boris', 'bondarenko', 29)
print(user.login_attempts)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
