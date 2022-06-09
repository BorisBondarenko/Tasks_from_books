class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is: {self.restaurant_name}')
        print(f'Cuisine type of it is: {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is already open!')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'pistachio', 'choco']

    def show_flavors(self):
        print('Today we have this special flavors for you:')
        for flavor in self.flavors:
            print(f'- {flavor}')


ice_cream_restaurant = IceCreamStand('Icy', 'fast food')
ice_cream_restaurant.show_flavors()
