class Dog:
    """A simple attempt to model a Dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""

        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sittng in response to command"""

        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate a dog roll over in response to command"""

        print(f"{self.name} rolled over!")


my_dog = Dog('lucky', 3)

print(f"My Dog's name is {my_dog.name}.")
print(f"My Dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
