class User:
    def __init__(self, first_name, last_time, sex, age, country):
        self.first_name = first_name
        self.last_name = last_time
        self.sex = sex
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"""
    Username: {self.first_name} {self.last_name}  
    Sex: {self.sex}
    Age: {self.age}
    Country: {self.country}  
        """)

    def greet_user(self):
        print(f""" 
    Bonjour {self.first_name} 'Your special greeting for {self.country}'

        """)


ayume = User('Ayume', 'Francis', 'Male', 22, 'South Sudan')
emma = User('Emma', 'Pussy', 'Male', 26, 'South Sudan')
renny = User('Renny', 'Tricia', 'Female', 18, ' Uganda')


ayume.describe_user()
ayume.greet_user()

emma.describe_user()
emma.greet_user()


renny.describe_user()
renny.greet_user()



