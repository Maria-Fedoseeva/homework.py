class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Curent speed: {}.'.format(self.speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Red', 'Sport Car', False)
town_car = TownCar(100, 'Gray', 'Town Car', False)
work_car = WorkCar(30, 'Yellow', 'Work Car', False)
police_car = PoliceCar(150, 'Blue', 'Police Car', True)

sport_car.go()
sport_car.stop()
sport_car.turn('left')
sport_car.show_speed()

town_car.go()
town_car.stop()
town_car.turn('right')
town_car.show_speed()

work_car.go()
work_car.stop()
work_car.turn('left')
work_car.show_speed()

police_car.go()
police_car.stop()
police_car.turn('right')
police_car.show_speed()
