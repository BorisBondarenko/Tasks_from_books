class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is: {self.restaurant_name}')
        print(f'Cuisine type of it is: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is already open!')


new_restaurant = Restaurant('Globus', 'China')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
