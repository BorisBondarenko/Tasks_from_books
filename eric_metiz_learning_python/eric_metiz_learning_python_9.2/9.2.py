class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is: {self.restaurant_name}')
        print(f'Cuisine type of it is: {self.cuisine_type}\n')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is already open!')


rest_1 = Restaurant('Globus', 'Czech bistro')
rest_2 = Restaurant('Who is Pho?', 'China')
rest_3 = Restaurant('M\'cdonalds', 'Fast foods')

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()
