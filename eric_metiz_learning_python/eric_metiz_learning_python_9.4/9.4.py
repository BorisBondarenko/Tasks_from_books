class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name is: {self.restaurant_name}')
        print(f'Cuisine type of it is: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is already open!\n')

    def set_number_served(self, number):
        self.number_served = number
        print(f'Number of served person was changed {number}!\n')

    def increment_number_served(self, increment):
        if increment > 0:
            self.number_served += increment
        else:
            print(f'Increment could not be negative: {increment}')


restaurant = Restaurant('Globus', 'bistro')
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(25)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(-2)
print(restaurant.number_served)
