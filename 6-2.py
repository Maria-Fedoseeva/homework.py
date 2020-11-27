class Road:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass

my_road = Road(100, 30)
print(my_road.calc_mass(), 'т.')
