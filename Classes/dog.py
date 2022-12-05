class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is sitting.')

    def roll_over(self):
        print(f'{self.name} rolled over.')

    def jump(self):
        print(f'{self.name} jumped up.')


my_dog = Dog('Lucky', 3)
his_dog = Dog('Tom', 3)
her_dog = Dog('Jerry', 5)


my_dog.sit()
his_dog.roll_over()
her_dog.jump()

print(my_dog.name)
print(his_dog.name)
print(her_dog.name)


