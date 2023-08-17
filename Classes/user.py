class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempt = 0

    def describe_user(self):
        user_profile = {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age, 'sex': self.sex}
        print(user_profile)

    def greet_user(self):
        print(f'Bonjour {self.first_name} {self.last_name}')

    def increment_login_attempt(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


print('\n')
ayudmin = User('ayud', 'min', 23, 'male')
ayudmin.describe_user()
print(ayudmin.login_attempt
)
ayudmin.increment_login_attempt()
ayudmin.increment_login_attempt()
ayudmin.increment_login_attempt()
ayudmin.increment_login_attempt()
print(ayudmin.login_attempt
)
ayudmin.reset_login_attempts()
print(ayudmin.login_attempt)
ayudmin.greet_user()
