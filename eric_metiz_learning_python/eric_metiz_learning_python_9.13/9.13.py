from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


my_cube_1 = Die()

for i in range(10):
    my_cube_1.roll_die()

my_cube_2 = Die(10)
for i in range(10):
    my_cube_2.roll_die()

my_cube_3 = Die(20)
for i in range(10):
    my_cube_3.roll_die()

