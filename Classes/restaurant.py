class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant: {self.name}, Cuisine: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.name} is open now.')


restaurant1 = Restaurant('Vino', 'Caribbean')
# print(new_restaurant.name)
# print(new_restaurant.cuisine_type)
#
# describe = new_restaurant.describe_restaurant()
# open = new_restaurant.open_restaurant()


restaurant2 = Restaurant('Pacific', 'Vietnamese')
restaurant3 = Restaurant('Hilltop', 'German')


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



