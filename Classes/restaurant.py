class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers

    def increment_number_served(self, number_of_customers):
        self.number_served += number_of_customers


restaurant = Restaurant('Istanbul', 'Pizaa')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.set_number_served(10)
restaurant.increment_number_served(10)
print(restaurant.number_served)

restaurant.describe_restaurant()
restaurant.open_restaurant()

second_restaurant = Restaurant('Mama Tabia', 'Mula Kombo')
second_restaurant.describe_restaurant()
