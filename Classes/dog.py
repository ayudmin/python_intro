class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")


my_dog = Dog('Willie', 6)
print(f"My dog name is: {my_dog.name}.")
print(f"My dog age is: {my_dog.age}.")
my_dog.sit()
print('\n')

my_dog_1 = Dog('Willie', 6)
print(f"My dog name is: {my_dog_1.name}.")
print(f"My dog age is: {my_dog_1.age}.")
my_dog_1.sit()
print('\n')

anotherDog = Dog('papy', 2)
print(anotherDog.name)
print(anotherDog.age)
my_dog.roll_over()
