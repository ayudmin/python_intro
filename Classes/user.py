class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        user_profile = {}
        user_profile['first_name'] =  self.first_name
        user_profile[ 'last_name'] = self.last_name
        user_profile['age'] = self.age
        user_profile['sex'] = self.sex
        print(user_profile)

    def greet_user(self):
        print(f'Bonjour {self.first_name} {self.last_name}')

ayudmin = User('ayud', 'min', 23, 'male')
ayudmin.describe_user()
ayudmin.greet_user()
print('\n')
user_new = User('ayume', 'francis', 23, 'male')
user_new.describe_user()
user_new.greet_user()
