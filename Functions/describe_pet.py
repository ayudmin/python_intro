def describe_pet(animal_type, animal_pet_name='dog'):
    print(f"I have a {animal_type.title()}")
    print(f"My {animal_type.title()}'s name is {animal_pet_name.title()}")

describe_pet('dog', 'brazillian hog')
print('\n')
describe_pet('cat', 'mick')
print('\n')
describe_pet(animal_type='Lion', animal_pet_name='Joan')
print('\n')
describe_pet('test', 'test')
print('\n')
describe_pet('test')